"""Compare drainage basins in erosion test inputs and outputs.

For each test input with a matching ``*-eroded-heightmap.png`` result, this
script writes an RGB basin comparison image beside the existing result images:

- red marks basins in the original input heightmap;
- blue marks basins in the eroded heightmap;
- green marks basins in the blurred input heightmap;
- overlaps add in RGB space.

Requires Pillow.
"""

#%%

from __future__ import annotations

import heapq
import math
from pathlib import Path

from PIL import Image, ImageFilter


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "test-inputs"
RESULT_DIR = BASE_DIR / "test-input-results"
MIN_FILL = 1
BLUR_SIGMA_FRACTION = 0.01
SIMPLE_RENDER_WATER_LEVEL = 0.15
SIMPLE_RENDER_HEIGHT_EXAGGERATION = 8
SIMPLE_RENDER_LIGHT_LENGTH = math.hypot(-0.5, -0.7, 0.5)
SIMPLE_RENDER_LIGHT = (
    -0.5 / SIMPLE_RENDER_LIGHT_LENGTH,
    -0.7 / SIMPLE_RENDER_LIGHT_LENGTH,
    0.5 / SIMPLE_RENDER_LIGHT_LENGTH,
)
SIMPLE_RENDER_COLOR_STOPS = (
    (0.00, 20, 55, 122),
    (SIMPLE_RENDER_WATER_LEVEL * 0.6, 45, 112, 176),
    (SIMPLE_RENDER_WATER_LEVEL, 226, 204, 122),
    (0.24, 118, 153, 76),
    (0.52, 93, 117, 66),
    (0.76, 120, 94, 70),
    (1.00, 243, 243, 235),
)
NEIGHBORS = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1),
)


def load_grayscale(path: Path) -> tuple[list[int], int, int]:
    image = Image.open(path).convert("L")
    width, height = image.size
    return list(image.getdata()), width, height


def load_blurred_grayscale(path: Path, sigma: float) -> tuple[list[int], int, int]:
    image = Image.open(path).convert("L").filter(ImageFilter.GaussianBlur(radius=sigma))
    width, height = image.size
    return list(image.getdata()), width, height


def basin_mask(
    heights: list[int],
    width: int,
    height: int,
    min_fill: int,
) -> list[bool]:
    """Return pixels whose priority-flood fill level is above the source height."""
    fill = [0] * (width * height)
    seen = bytearray(width * height)
    heap: list[tuple[int, int]] = []

    def push(index: int, level: int) -> None:
        if seen[index]:
            return
        seen[index] = 1
        fill[index] = level
        heapq.heappush(heap, (level, index))

    for x in range(width):
        push(x, heights[x])
        bottom = (height - 1) * width + x
        push(bottom, heights[bottom])

    for y in range(1, height - 1):
        left = y * width
        push(left, heights[left])
        right = left + width - 1
        push(right, heights[right])

    neighbors = (
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1),
    )

    while heap:
        level, index = heapq.heappop(heap)
        x = index % width
        y = index // width
        for dx, dy in neighbors:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            neighbor = ny * width + nx
            if seen[neighbor]:
                continue
            push(neighbor, max(level, heights[neighbor]))

    return [fill[i] - heights[i] >= min_fill for i in range(width * height)]


def write_comparison(
    output_path: Path,
    input_mask: list[bool],
    blurred_mask: list[bool],
    eroded_mask: list[bool],
    width: int,
    height: int,
) -> None:
    pixels = [
        (
            255 if input_mask[i] else 0,
            255 if blurred_mask[i] else 0,
            255 if eroded_mask[i] else 0,
        )
        for i in range(width * height)
    ]
    image = Image.new("RGB", (width, height))
    image.putdata(pixels)
    image.save(output_path)


def new_eroded_basin_components(
    input_mask: list[bool],
    eroded_mask: list[bool],
    width: int,
    height: int,
) -> list[list[int]]:
    """Return eroded basin components that do not overlap an input basin."""
    components = []
    seen = bytearray(width * height)

    for start in range(width * height):
        if seen[start] or not eroded_mask[start]:
            continue

        component = []
        touches_input_basin = False
        stack = [start]
        seen[start] = 1

        while stack:
            index = stack.pop()
            component.append(index)
            touches_input_basin = touches_input_basin or input_mask[index]
            x = index % width
            y = index // width

            for dx, dy in NEIGHBORS:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue
                neighbor = ny * width + nx
                if seen[neighbor] or not eroded_mask[neighbor]:
                    continue
                seen[neighbor] = 1
                stack.append(neighbor)

        if not touches_input_basin:
            components.append(component)

    return components


def component_mask(components: list[list[int]], size: int) -> list[bool]:
    new_basin = [False] * size
    for component in components:
        for index in component:
            new_basin[index] = True
    return new_basin


def write_lake_overlay(
    render_path: Path,
    output_path: Path,
    lake_mask: list[bool],
    width: int,
    height: int,
) -> None:
    image = Image.open(render_path).convert("RGB")
    if image.size != (width, height):
        print(f"Skipping {render_path.stem}: render and mask sizes differ.")
        return

    pixels = list(image.getdata())
    for i, is_lake in enumerate(lake_mask):
        if is_lake:
            pixels[i] = (0, 0, 255)
    image.putdata(pixels)
    image.save(output_path)


def write_grayscale(path: Path, heights: list[int], width: int, height: int) -> None:
    image = Image.new("L", (width, height))
    image.putdata(heights)
    image.save(path)


def fill_basins_to_lowest_edge(
    heights: list[int],
    components: list[list[int]],
    width: int,
    height: int,
) -> list[int]:
    filled = heights.copy()
    active = bytearray(width * height)

    for component in components:
        for index in component:
            active[index] = 1

        edge_height = None
        for index in component:
            x = index % width
            y = index // width
            for dx, dy in NEIGHBORS:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue
                neighbor = ny * width + nx
                if active[neighbor]:
                    continue
                if edge_height is None or heights[neighbor] < edge_height:
                    edge_height = heights[neighbor]

        if edge_height is not None:
            for index in component:
                filled[index] = edge_height

        for index in component:
            active[index] = 0

    return filled


def clamp(value: float, low: float, high: float) -> float:
    return min(max(value, low), high)


def sample_height(values: list[int], width: int, height: int, x: int, y: int) -> float:
    x = round(clamp(x, 0, width - 1))
    y = round(clamp(y, 0, height - 1))
    return values[y * width + x] / 255


def simple_bump_shade(values: list[int], width: int, height: int, x: int, y: int) -> float:
    west = sample_height(values, width, height, x - 1, y)
    east = sample_height(values, width, height, x + 1, y)
    north = sample_height(values, width, height, x, y - 1)
    south = sample_height(values, width, height, x, y + 1)
    horizontal_scale = max(width, height) * 0.5
    nx = -(east - west) * horizontal_scale * SIMPLE_RENDER_HEIGHT_EXAGGERATION
    ny = -(south - north) * horizontal_scale * SIMPLE_RENDER_HEIGHT_EXAGGERATION
    nz = 1
    normal_length = math.sqrt(nx * nx + ny * ny + nz * nz)
    lambert = clamp(
        (
            nx * SIMPLE_RENDER_LIGHT[0]
            + ny * SIMPLE_RENDER_LIGHT[1]
            + nz * SIMPLE_RENDER_LIGHT[2]
        ) / normal_length,
        0,
        1,
    )
    return 0.58 + lambert * 0.48


def simple_render_color(height_value: float) -> tuple[float, float, float]:
    value = clamp(height_value, 0, 1)
    for i in range(1, len(SIMPLE_RENDER_COLOR_STOPS)):
        low = SIMPLE_RENDER_COLOR_STOPS[i - 1]
        high = SIMPLE_RENDER_COLOR_STOPS[i]
        if value <= high[0]:
            t = (value - low[0]) / (high[0] - low[0])
            return (
                low[1] + (high[1] - low[1]) * t,
                low[2] + (high[2] - low[2]) * t,
                low[3] + (high[3] - low[3]) * t,
            )
    return (243, 243, 235)


def write_simple_render(path: Path, heights: list[int], width: int, height: int) -> None:
    pixels = []
    for y in range(height):
        for x in range(width):
            index = y * width + x
            shade = simple_bump_shade(heights, width, height, x, y)
            color = simple_render_color(heights[index] / 255)
            pixels.append(tuple(round(clamp(channel * shade, 0, 255)) for channel in color))

    image = Image.new("RGB", (width, height))
    image.putdata(pixels)
    image.save(path)


def matching_pairs(input_dir: Path, result_dir: Path) -> list[tuple[Path, Path, str]]:
    pairs = []
    suffix = "-eroded-heightmap.png"
    for eroded_path in sorted(result_dir.glob(f"*{suffix}")):
        name = eroded_path.name
        input_stem = name[:-len(suffix)]
        input_path = input_dir / f"{input_stem}.png"
        if input_path.exists():
            pairs.append((input_path, eroded_path, input_stem))
    return pairs


pairs = matching_pairs(INPUT_DIR, RESULT_DIR)
if not pairs:
    raise SystemExit("No matching input/result pairs found.")

for input_path, eroded_path, stem in pairs:
    input_heights, width, height = load_grayscale(input_path)
    blurred_heights, blurred_width, blurred_height = load_blurred_grayscale(
        input_path,
        width * BLUR_SIGMA_FRACTION,
    )
    eroded_heights, eroded_width, eroded_height = load_grayscale(eroded_path)
    if (blurred_width, blurred_height) != (width, height):
        print(f"Skipping {stem}: input and blurred image sizes differ.")
        continue
    if (eroded_width, eroded_height) != (width, height):
        print(f"Skipping {stem}: input and eroded image sizes differ.")
        continue

    input_basins = basin_mask(input_heights, width, height, MIN_FILL)
    blurred_basins = basin_mask(blurred_heights, width, height, MIN_FILL)
    eroded_basins = basin_mask(eroded_heights, width, height, MIN_FILL)
    output_path = RESULT_DIR / f"{stem}-basin-comparison.png"
    write_comparison(output_path, input_basins, blurred_basins, eroded_basins, width, height)
    print(f"Wrote {output_path}")

    lake_components = new_eroded_basin_components(input_basins, eroded_basins, width, height)
    lake_mask = component_mask(lake_components, width * height)
    render_path = RESULT_DIR / f"{stem}-eroded-heightmap-colormap.png"
    if not render_path.exists():
        print(f"Skipping {stem}: no colormap render found.")
        continue
    lake_output_path = RESULT_DIR / f"{stem}-eroded-heightmap-colormap-lakes.png"
    write_lake_overlay(render_path, lake_output_path, lake_mask, width, height)
    print(f"Wrote {lake_output_path}")

    blur_lake_components = new_eroded_basin_components(blurred_basins, eroded_basins, width, height)
    blur_lake_mask = component_mask(blur_lake_components, width * height)
    blur_lake_output_path = RESULT_DIR / f"{stem}-eroded-heightmap-colormap-lakes-blur.png"
    write_lake_overlay(render_path, blur_lake_output_path, blur_lake_mask, width, height)
    print(f"Wrote {blur_lake_output_path}")

    filled_heights = fill_basins_to_lowest_edge(
        eroded_heights,
        blur_lake_components,
        width,
        height,
    )
    filled_path = RESULT_DIR / f"{stem}-eroded-heightmap-filled.png"
    write_grayscale(filled_path, filled_heights, width, height)
    print(f"Wrote {filled_path}")

    filled_render_path = RESULT_DIR / f"{stem}-eroded-heightmap-colormap-filled.png"
    write_simple_render(filled_render_path, filled_heights, width, height)
    print(f"Wrote {filled_render_path}")

# %%
