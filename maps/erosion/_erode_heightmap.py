from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


# Fresh CPU translation of the ShaderToy heightmap erosion pass in this folder.
# The source erosion filter is by Rune Skovbo Johansen and licensed MPL 2.0.

TAU = 6.28318530717959
DEFAULT_PREBLUR_SIGMA = 0.85
DEFAULT_DEQUANTIZE_LSB = 1.0
DEFAULT_DITHER_LSB = 0.75


def clamp01(x: np.ndarray) -> np.ndarray:
    return np.clip(x, 0.0, 1.0)


def fract(x: np.ndarray) -> np.ndarray:
    return x - np.floor(x)


def mix(a: np.ndarray | float, b: np.ndarray | float, t: np.ndarray | float) -> np.ndarray:
    return np.asarray(a) * (1.0 - t) + np.asarray(b) * t


def shader_hash(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    kx = 0.3183099
    ky = 0.3678794
    x2 = x * kx + ky
    y2 = y * ky + kx
    f = fract(x2 * y2 * (x2 + y2))
    return -1.0 + 2.0 * fract(16.0 * kx * f), -1.0 + 2.0 * fract(16.0 * ky * f)


def pow_inv(t: np.ndarray, power: float) -> np.ndarray:
    return 1.0 - np.power(1.0 - clamp01(t), power)


def ease_out(t: np.ndarray) -> np.ndarray:
    v = 1.0 - clamp01(t)
    return 1.0 - v * v


def smooth_start(t: np.ndarray, smoothing: np.ndarray) -> np.ndarray:
    out = t - 0.5 * smoothing
    mask = (t < smoothing) & (smoothing > 1e-12)
    out[mask] = 0.5 * t[mask] * t[mask] / smoothing[mask]
    return out


def safe_normalize(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    length = np.sqrt(x * x + y * y)
    safe = length > 1e-10
    return np.divide(x, length, out=np.zeros_like(x), where=safe), np.divide(y, length, out=np.zeros_like(y), where=safe)


def phacelle_noise(
    px: np.ndarray,
    py: np.ndarray,
    norm_x: np.ndarray,
    norm_y: np.ndarray,
    freq: float,
    offset: float,
    normalization: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    side_x = -norm_y * freq * TAU
    side_y = norm_x * freq * TAU
    phase_offset = offset * TAU

    p_int_x = np.floor(px)
    p_int_y = np.floor(py)
    p_frac_x = px - p_int_x
    p_frac_y = py - p_int_y

    phase_x = np.zeros_like(px)
    phase_y = np.zeros_like(px)
    weight_sum = np.zeros_like(px)

    for i in range(-1, 3):
        for j in range(-1, 3):
            grid_x = p_int_x + i
            grid_y = p_int_y + j
            rand_x, rand_y = shader_hash(grid_x, grid_y)
            vx = p_frac_x - i - rand_x * 0.5
            vy = p_frac_y - j - rand_y * 0.5

            sqr_dist = vx * vx + vy * vy
            weight = np.maximum(0.0, np.exp(-sqr_dist * 2.0) - 0.01111)
            wave_input = vx * side_x + vy * side_y + phase_offset

            phase_x += np.cos(wave_input) * weight
            phase_y += np.sin(wave_input) * weight
            weight_sum += weight

    interpolated_x = phase_x / np.maximum(weight_sum, 1e-12)
    interpolated_y = phase_y / np.maximum(weight_sum, 1e-12)
    magnitude = np.sqrt(interpolated_x * interpolated_x + interpolated_y * interpolated_y)
    magnitude = np.maximum(1.0 - normalization, magnitude)

    return interpolated_x / magnitude, interpolated_y / magnitude, side_x, side_y


def source_slope(height: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    padded = np.pad(height, 1, mode="edge")
    h_left = padded[1:-1, :-2]
    h_right = padded[1:-1, 2:]
    h_down = padded[:-2, 1:-1]
    h_up = padded[2:, 1:-1]
    rows, cols = height.shape
    return (h_right - h_left) * cols * 0.5, (h_up - h_down) * rows * 0.5


def gaussian_kernel(sigma: float) -> np.ndarray:
    radius = max(1, int(np.ceil(sigma * 3.0)))
    x = np.arange(-radius, radius + 1, dtype=np.float64)
    kernel = np.exp(-(x * x) / (2.0 * sigma * sigma))
    return kernel / kernel.sum()


def blur_axis(image: np.ndarray, kernel: np.ndarray, axis: int) -> np.ndarray:
    radius = len(kernel) // 2
    pad = [(0, 0), (0, 0)]
    pad[axis] = (radius, radius)
    padded = np.pad(image, pad, mode="edge")
    out = np.zeros_like(image)
    for i, weight in enumerate(kernel):
        if axis == 0:
            out += padded[i : i + image.shape[0], :] * weight
        else:
            out += padded[:, i : i + image.shape[1]] * weight
    return out


def gaussian_blur(image: np.ndarray, sigma: float) -> np.ndarray:
    if sigma <= 0.0:
        return image
    kernel = gaussian_kernel(sigma)
    return blur_axis(blur_axis(image, kernel, axis=1), kernel, axis=0)


def dequantize_height(height: np.ndarray, lsb_amplitude: float) -> np.ndarray:
    if lsb_amplitude <= 0.0:
        return height
    rows, cols = height.shape
    yy, xx = np.mgrid[0:rows, 0:cols]
    n1, _ = shader_hash(xx.astype(np.float64), yy.astype(np.float64))
    n2, _ = shader_hash(xx.astype(np.float64) + 19.19, yy.astype(np.float64) - 7.31)
    tpdf = (n1 + n2) * 0.5
    return np.clip(height + tpdf * (lsb_amplitude / 255.0), 0.0, 1.0)


def prepare_height(height: np.ndarray, preblur_sigma: float, dequantize_lsb: float) -> np.ndarray:
    height = dequantize_height(height, dequantize_lsb)
    height = gaussian_blur(height, preblur_sigma)
    return np.clip(height, 0.0, 1.0)


def dithered_u8(height: np.ndarray, dither_lsb: float) -> np.ndarray:
    if dither_lsb <= 0.0:
        return np.round(np.clip(height, 0.0, 1.0) * 255.0).astype(np.uint8)

    rows, cols = height.shape
    yy, xx = np.mgrid[0:rows, 0:cols]
    n1, _ = shader_hash(xx.astype(np.float64) + 101.7, yy.astype(np.float64) - 53.2)
    n2, _ = shader_hash(xx.astype(np.float64) - 17.4, yy.astype(np.float64) + 211.9)
    tpdf = (n1 + n2) * 0.5
    quantized = np.clip(height + tpdf * (dither_lsb / 255.0), 0.0, 1.0)
    return np.round(quantized * 255.0).astype(np.uint8)


def erode_heightmap(height: np.ndarray, preblur_sigma: float, dequantize_lsb: float) -> np.ndarray:
    height = prepare_height(height, preblur_sigma, dequantize_lsb)
    rows, cols = height.shape
    yy, xx = np.mgrid[0:rows, 0:cols]
    px = (xx.astype(np.float64) + 0.5) / cols
    py = (yy.astype(np.float64) + 0.5) / rows

    slope_x, slope_y = source_slope(height)
    h = height.astype(np.float64).copy()
    sx = slope_x.astype(np.float64)
    sy = slope_y.astype(np.float64)

    scale = 0.15
    strength = 0.22 * scale
    gully_weight = 0.5
    detail = 1.5
    rounding = np.array([0.1, 0.0, 0.1, 2.0], dtype=np.float64)
    onset = np.array([0.7, 1.25, 2.8, 1.5], dtype=np.float64)
    assumed_slope = np.array([0.7, 1.0], dtype=np.float64)
    octaves = 5
    lacunarity = 2.0
    gain = 0.5
    cell_scale = 0.7
    normalization = 0.5

    fade_target = np.clip((h - 0.45) / 0.15, -1.0, 1.0)
    input_h = h.copy()

    freq = 1.0 / (scale * cell_scale)
    slope_length = np.maximum(np.sqrt(sx * sx + sy * sy), 1e-10)
    magnitude = 0.0
    rounding_mult = 1.0

    rounding_for_input = mix(rounding[1], rounding[0], clamp01(fade_target + 0.5)) * rounding[2]
    combi_mask = ease_out(smooth_start(slope_length * onset[0], rounding_for_input * onset[0]))

    gully_base_x = sx / slope_length * assumed_slope[0]
    gully_base_y = sy / slope_length * assumed_slope[0]
    gully_slope_x = mix(sx, gully_base_x, assumed_slope[1])
    gully_slope_y = mix(sy, gully_base_y, assumed_slope[1])

    for _ in range(octaves):
        norm_x, norm_y = safe_normalize(gully_slope_x, gully_slope_y)
        ph_x, ph_y, ph_z, ph_w = phacelle_noise(
            px * freq,
            py * freq,
            norm_x,
            norm_y,
            cell_scale,
            0.25,
            normalization,
        )
        ph_z *= -freq
        ph_w *= -freq

        sloping = np.abs(ph_y)
        sign_y = np.sign(ph_y)
        gully_slope_x += sign_y * ph_z * strength * gully_weight
        gully_slope_y += sign_y * ph_w * strength * gully_weight

        gullies_h = ph_x
        gullies_x = ph_y * ph_z
        gullies_y = ph_y * ph_w

        faded_h = mix(fade_target, gullies_h * gully_weight, combi_mask)
        faded_x = gullies_x * gully_weight * combi_mask
        faded_y = gullies_y * gully_weight * combi_mask

        h += faded_h * strength
        sx += faded_x * strength
        sy += faded_y * strength
        magnitude += strength
        fade_target = faded_h

        rounding_for_octave = mix(rounding[1], rounding[0], clamp01(ph_x + 0.5)) * rounding_mult
        new_mask = ease_out(smooth_start(sloping * onset[1], rounding_for_octave * onset[1]))
        combi_mask = pow_inv(combi_mask, detail) * new_mask

        strength *= gain
        freq *= lacunarity
        rounding_mult *= rounding[3]

    height_delta = h - input_h
    if magnitude <= 0.0:
        return height
    return np.clip(height + height_delta, 0.0, 1.0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply the ShaderToy erosion height filter to a grayscale heightmap.")
    parser.add_argument("input", type=Path, nargs="?", default=Path("test_blob.png"))
    parser.add_argument("--preblur-sigma", type=float, default=DEFAULT_PREBLUR_SIGMA)
    parser.add_argument("--dequantize-lsb", type=float, default=DEFAULT_DEQUANTIZE_LSB)
    parser.add_argument("--dither-lsb", type=float, default=DEFAULT_DITHER_LSB)
    parser.add_argument("--bit-depth", type=int, choices=(8, 16), default=8)
    args = parser.parse_args()

    source = args.input
    if not source.is_absolute():
        source = Path(__file__).resolve().parent / source

    height = np.asarray(Image.open(source).convert("L"), dtype=np.float64) / 255.0
    eroded = erode_heightmap(height, args.preblur_sigma, args.dequantize_lsb)

    output = source.with_name(f"eroded_{source.name}")
    if args.bit_depth == 16:
        image = Image.fromarray(np.round(eroded * 65535.0).astype(np.uint16))
    else:
        image = Image.fromarray(dithered_u8(eroded, args.dither_lsb))
    image.save(output)
    print(output)


if __name__ == "__main__":
    main()
