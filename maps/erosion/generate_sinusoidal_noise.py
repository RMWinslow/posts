"""Generate a smooth 1000x1000 grayscale sinusoidal-noise PNG.

The image is built by summing low-frequency sine waves with random directions,
wavelengths, phases, and amplitudes. It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import math
import random
import struct
import zlib
from pathlib import Path


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + chunk_type
        + data
        + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
    )


def write_grayscale_png(path: Path, width: int, height: int, pixels: bytearray) -> None:
    header = struct.pack(">IIBBBBB", width, height, 8, 0, 0, 0, 0)
    rows = bytearray()
    stride = width
    for y in range(height):
        rows.append(0)
        start = y * stride
        rows.extend(pixels[start:start + stride])

    png = (
        b"\x89PNG\r\n\x1a\n"
        + png_chunk(b"IHDR", header)
        + png_chunk(b"IDAT", zlib.compress(bytes(rows), level=9))
        + png_chunk(b"IEND", b"")
    )
    path.write_bytes(png)


def generate_sinusoidal_noise(
    width: int,
    height: int,
    seed: int,
    waves: int,
    value_low: int,
    value_high: int,
) -> bytearray:
    rng = random.Random(seed)
    components = []
    for i in range(waves):
        angle = rng.uniform(0, math.tau)
        wavelength = rng.uniform(0.16, 0.75) * min(width, height)
        frequency = min(width, height) / wavelength
        amplitude = rng.uniform(0.45, 1.0) / (1 + i * 0.22)
        phase = rng.uniform(0, math.tau)
        components.append((math.cos(angle) * frequency, math.sin(angle) * frequency, amplitude, phase))

    values = [0.0] * (width * height)
    low = float("inf")
    high = float("-inf")

    for y in range(height):
        v = y / height
        for x in range(width):
            u = x / width
            value = 0.0
            for fx, fy, amplitude, phase in components:
                value += amplitude * math.sin(math.tau * (fx * u + fy * v) + phase)
            index = y * width + x
            values[index] = value
            low = min(low, value)
            high = max(high, value)

    scale = (value_high - value_low) / max(high - low, 1e-9)
    pixels = bytearray(width * height)
    for i, value in enumerate(values):
        pixels[i] = round(value_low + (value - low) * scale)
    return pixels


def main() -> None:
    default_output = Path(__file__).resolve().parent / "test-inputs" / "sinusoidal-noise.png"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output)
    parser.add_argument("--size", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--waves", type=int, default=24)
    parser.add_argument("--value-low", type=int, default=20)
    parser.add_argument("--value-high", type=int, default=220)
    args = parser.parse_args()

    if not 0 <= args.value_low < args.value_high <= 255:
        raise ValueError("Expected 0 <= value-low < value-high <= 255")

    pixels = generate_sinusoidal_noise(
        args.size,
        args.size,
        args.seed,
        args.waves,
        args.value_low,
        args.value_high,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_grayscale_png(args.output, args.size, args.size, pixels)
    print(f"Wrote {args.output} ({args.size}x{args.size})")


if __name__ == "__main__":
    main()
