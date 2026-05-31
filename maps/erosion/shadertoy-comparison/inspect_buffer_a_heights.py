"""Inspect Shadertoy Buffer A EXR height channels.

The exported Buffer A files store:
  R / x: normalized height in [0, 1]
  G / y: d(height) / d(normalized x)
  B / z: d(height) / d(normalized y)

This script intentionally implements only the small OpenEXR subset used by the
Shadertoy exports in this folder: scanline, uncompressed, FLOAT channels.
"""

from __future__ import annotations

import argparse
import csv
import struct
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


EXR_MAGIC = 20000630
EXR_VERSION = 2
TILED_FLAG = 0x200
DEEP_DATA_FLAG = 0x800
MULTIPART_FLAG = 0x1000
NO_COMPRESSION = 0
FLOAT_CHANNEL = 2
PIXEL_TYPE_BYTES = {
    0: 4,  # UINT
    1: 2,  # HALF
    2: 4,  # FLOAT
}


@dataclass(frozen=True)
class Channel:
    name: str
    pixel_type: int
    x_sampling: int
    y_sampling: int


@dataclass(frozen=True)
class ExrHeader:
    width: int
    height: int
    xmin: int
    ymin: int
    channels: tuple[Channel, ...]
    compression: int
    header_end: int


def read_cstring(data: bytes, offset: int) -> tuple[str, int]:
    end = data.index(b"\x00", offset)
    return data[offset:end].decode("ascii"), end + 1


def parse_channels(value: bytes) -> tuple[Channel, ...]:
    channels: list[Channel] = []
    offset = 0
    while offset < len(value):
        if value[offset] == 0:
            break
        name, offset = read_cstring(value, offset)
        pixel_type = struct.unpack_from("<I", value, offset)[0]
        offset += 4
        offset += 4  # pLinear byte plus three reserved bytes.
        x_sampling, y_sampling = struct.unpack_from("<ii", value, offset)
        offset += 8
        channels.append(Channel(name, pixel_type, x_sampling, y_sampling))
    return tuple(channels)


def parse_exr_header(data: bytes) -> ExrHeader:
    magic, version = struct.unpack_from("<II", data, 0)
    if magic != EXR_MAGIC:
        raise ValueError("Not an OpenEXR file.")
    if version & 0xFF != EXR_VERSION:
        raise ValueError(f"Unsupported OpenEXR version field: {version!r}")
    unsupported_flags = version & (TILED_FLAG | DEEP_DATA_FLAG | MULTIPART_FLAG)
    if unsupported_flags:
        raise ValueError(f"Unsupported OpenEXR layout flags: 0x{unsupported_flags:x}")

    offset = 8
    attrs: dict[str, tuple[str, bytes]] = {}
    while True:
        name, offset = read_cstring(data, offset)
        if not name:
            break
        attr_type, offset = read_cstring(data, offset)
        size = struct.unpack_from("<I", data, offset)[0]
        offset += 4
        attrs[name] = (attr_type, data[offset : offset + size])
        offset += size

    try:
        channels = parse_channels(attrs["channels"][1])
        compression = attrs["compression"][1][0]
        xmin, ymin, xmax, ymax = struct.unpack("<iiii", attrs["dataWindow"][1])
    except KeyError as exc:
        raise ValueError(f"Missing required EXR attribute: {exc.args[0]}") from exc

    image_type = attrs.get("type")
    if image_type is not None and image_type[1].decode("ascii").rstrip("\x00") != "scanlineimage":
        raise ValueError(f"Unsupported OpenEXR image type: {image_type[1]!r}")

    return ExrHeader(
        width=xmax - xmin + 1,
        height=ymax - ymin + 1,
        xmin=xmin,
        ymin=ymin,
        channels=channels,
        compression=compression,
        header_end=offset,
    )


def channel_dtype(pixel_type: int) -> np.dtype:
    if pixel_type == 0:
        return np.dtype("<u4")
    if pixel_type == 1:
        return np.dtype("<f2")
    if pixel_type == 2:
        return np.dtype("<f4")
    raise ValueError(f"Unsupported EXR channel pixel type: {pixel_type}")


def read_uncompressed_scanline_exr(path: Path) -> tuple[ExrHeader, dict[str, np.ndarray]]:
    data = path.read_bytes()
    header = parse_exr_header(data)

    if header.compression != NO_COMPRESSION:
        raise ValueError(f"{path.name}: expected uncompressed EXR, got compression={header.compression}.")

    for channel in header.channels:
        if channel.pixel_type != FLOAT_CHANNEL:
            raise ValueError(f"{path.name}: expected FLOAT channel {channel.name}, got type={channel.pixel_type}.")
        if channel.x_sampling != 1 or channel.y_sampling != 1:
            raise ValueError(f"{path.name}: unsupported channel sampling on {channel.name}.")

    chunk_count = header.height
    offset_table_start = header.header_end
    offset_table_end = offset_table_start + chunk_count * 8
    chunk_offsets = struct.unpack_from(f"<{chunk_count}Q", data, offset_table_start)

    arrays = {
        channel.name: np.empty((header.height, header.width), dtype=np.float32)
        for channel in header.channels
    }

    bytes_per_scanline = sum(PIXEL_TYPE_BYTES[channel.pixel_type] * header.width for channel in header.channels)
    for chunk_offset in chunk_offsets:
        y, data_size = struct.unpack_from("<iI", data, chunk_offset)
        if data_size != bytes_per_scanline:
            raise ValueError(f"{path.name}: unexpected scanline byte count at y={y}: {data_size}.")

        row = y - header.ymin
        cursor = chunk_offset + 8
        for channel in header.channels:
            count = header.width
            byte_count = PIXEL_TYPE_BYTES[channel.pixel_type] * count
            values = np.frombuffer(data, dtype=channel_dtype(channel.pixel_type), count=count, offset=cursor)
            arrays[channel.name][row, :] = values
            cursor += byte_count

    return header, arrays


def exact_mode(values: np.ndarray) -> tuple[float, int, float] | None:
    unique, counts = np.unique(values, return_counts=True)
    index = int(np.argmax(counts))
    count = int(counts[index])
    if count <= 1:
        return None
    return float(unique[index]), count, count / values.size


def summarize_height(path: Path, height: np.ndarray, kde_grid_size: int, kde_sample_size: int, rng: np.random.Generator) -> dict[str, float | int | str]:
    values = height[np.isfinite(height)].astype(np.float64)
    if values.size == 0:
        raise ValueError(f"{path.name}: height channel contains no finite values.")

    if np.all(values == values[0]):
        kde_mode = float(values[0])
    else:
        sample = values
        if values.size > kde_sample_size:
            sample = rng.choice(values, size=kde_sample_size, replace=False)
        grid = np.linspace(float(values.min()), float(values.max()), kde_grid_size)
        kde = gaussian_kde(sample)
        density = kde(grid)
        kde_mode = float(grid[int(np.argmax(density))])

    mode = exact_mode(values)
    exact_mode_value = np.nan if mode is None else mode[0]
    exact_mode_count = 1 if mode is None else mode[1]
    exact_mode_share = exact_mode_count / values.size if mode is None else mode[2]

    return {
        "file": path.name,
        "width": height.shape[1],
        "height": height.shape[0],
        "pixels": int(values.size),
        "min": float(values.min()),
        "p01": float(np.quantile(values, 0.01)),
        "p05": float(np.quantile(values, 0.05)),
        "median": float(np.median(values)),
        "mean": float(np.mean(values)),
        "p95": float(np.quantile(values, 0.95)),
        "p99": float(np.quantile(values, 0.99)),
        "max": float(values.max()),
        "std": float(np.std(values)),
        "exact_mode": exact_mode_value,
        "exact_mode_count": exact_mode_count,
        "exact_mode_share": exact_mode_share,
        "kde_mode": kde_mode,
    }


def write_markdown_table(rows: list[dict[str, float | int | str]], path: Path) -> None:
    columns = [
        "file",
        "min",
        "median",
        "max",
        "exact_mode",
        "exact_mode_share",
        "kde_mode",
        "mean",
        "std",
    ]
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        formatted = []
        for column in columns:
            value = row[column]
            if isinstance(value, float):
                formatted.append("" if np.isnan(value) else f"{value:.6g}")
            else:
                formatted.append(str(value))
        lines.append("| " + " | ".join(formatted) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def plot_kdes(files: list[Path], output_path: Path, kde_grid_size: int, kde_sample_size: int, rng: np.random.Generator) -> None:
    plt.figure(figsize=(9, 5.5))
    for path in files:
        _, arrays = read_uncompressed_scanline_exr(path)
        height = arrays["R"][np.isfinite(arrays["R"])].astype(np.float64)
        if np.all(height == height[0]):
            plt.axvline(float(height[0]), linewidth=2, label=f"{path.stem} (constant)")
            continue
        sample = height
        if height.size > kde_sample_size:
            sample = rng.choice(height, size=kde_sample_size, replace=False)
        grid = np.linspace(float(height.min()), float(height.max()), kde_grid_size)
        density = gaussian_kde(sample)(grid)
        plt.plot(grid, density, linewidth=2, label=path.stem)

    plt.title("Buffer A height channel density")
    plt.xlabel("Normalized height, R/x channel")
    plt.ylabel("Kernel density")
    plt.xlim(0, 1)
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="Buffer A EXR files. Defaults to *-buffer-a.exr in this script's folder.",
    )
    parser.add_argument("--csv", type=Path, default=None, help="Output CSV path.")
    parser.add_argument("--markdown", type=Path, default=None, help="Output Markdown table path.")
    parser.add_argument("--plot", type=Path, default=None, help="Output PyPlot KDE image path.")
    parser.add_argument("--kde-grid-size", type=int, default=512)
    parser.add_argument("--kde-sample-size", type=int, default=120_000)
    parser.add_argument("--seed", type=int, default=12345)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_dir = Path(__file__).resolve().parent
    files = args.files or sorted(base_dir.glob("*-buffer-a.exr"))
    files = [path if path.is_absolute() else (Path.cwd() / path) for path in files]

    if not files:
        raise SystemExit("No Buffer A EXR files found.")

    output_csv = args.csv or base_dir / "buffer_a_height_stats.csv"
    output_markdown = args.markdown or base_dir / "buffer_a_height_stats.md"
    output_plot = args.plot or base_dir / "buffer_a_height_density.png"

    rng = np.random.default_rng(args.seed)
    rows: list[dict[str, float | int | str]] = []
    for path in files:
        header, arrays = read_uncompressed_scanline_exr(path)
        if "R" not in arrays:
            raise ValueError(f"{path.name}: no R channel found. Channels: {', '.join(arrays)}")
        row = summarize_height(path, arrays["R"], args.kde_grid_size, args.kde_sample_size, rng)
        row["channels"] = ",".join(channel.name for channel in header.channels)
        row["format"] = "uncompressed scanline OpenEXR, FLOAT channels"
        rows.append(row)

    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    write_markdown_table(rows, output_markdown)
    plot_kdes(files, output_plot, args.kde_grid_size, args.kde_sample_size, rng)

    print(f"Wrote {output_csv}")
    print(f"Wrote {output_markdown}")
    print(f"Wrote {output_plot}")


if __name__ == "__main__":
    main()
