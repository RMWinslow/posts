from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


STEPS = (
    (0.00, (28, 82, 135)),    # water
    (0.20, (222, 197, 118)),  # sand
    (0.30, (72, 136, 68)),    # lowland
    (0.52, (126, 112, 72)),   # upland
    (0.72, (232, 232, 224)),  # snow
)


def load_height(path: Path) -> np.ndarray:
    image = Image.open(path)
    arr = np.asarray(image)
    if arr.ndim == 3:
        arr = np.asarray(image.convert("L"))

    if np.issubdtype(arr.dtype, np.integer):
        max_value = np.iinfo(arr.dtype).max
    else:
        max_value = arr.max()
    arr = arr.astype(np.float64)
    if max_value <= 0:
        return np.zeros(arr.shape, dtype=np.float64)
    return np.clip(arr / max_value, 0.0, 1.0)


def colorize(height: np.ndarray) -> np.ndarray:
    colors = np.zeros((*height.shape, 3), dtype=np.float64)
    step_colors = [(threshold, np.array(color, dtype=np.float64) / 255.0) for threshold, color in STEPS]

    for threshold, color in step_colors:
        colors[height >= threshold] = color
    return colors


def hillshade(height: np.ndarray, strength: float) -> np.ndarray:
    padded = np.pad(height, 1, mode="edge")
    dzdx = (padded[1:-1, 2:] - padded[1:-1, :-2]) * 0.5
    dzdy = (padded[2:, 1:-1] - padded[:-2, 1:-1]) * 0.5

    normal = np.dstack((-dzdx * strength, -dzdy * strength, np.ones_like(height)))
    normal /= np.maximum(np.linalg.norm(normal, axis=2, keepdims=True), 1e-12)

    light = np.array([-0.45, -0.55, 0.72], dtype=np.float64)
    light /= np.linalg.norm(light)
    shade = np.clip(np.sum(normal * light, axis=2), 0.0, 1.0)
    return 0.55 + shade * 0.65


def render(height: np.ndarray, shadow_strength: float) -> np.ndarray:
    colors = colorize(height)
    shade = hillshade(height, shadow_strength)
    rendered = np.clip(colors * shade[..., None], 0.0, 1.0)
    return np.round(rendered * 255.0).astype(np.uint8)


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply stepped terrain colors and a simple hillshade to a heightmap.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--shadow-strength", type=float, default=90.0)
    args = parser.parse_args()

    source = args.input
    if not source.is_absolute():
        source = Path(__file__).resolve().parent / source

    height = load_height(source)
    rendered = render(height, args.shadow_strength)

    output = source.with_name(f"rendered_{source.name}")
    Image.fromarray(rendered, mode="RGB").save(output)
    print(output)


if __name__ == "__main__":
    main()
