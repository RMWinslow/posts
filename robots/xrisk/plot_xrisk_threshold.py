"""
Plot AGI-button threshold contours from ../xrisk.md.

For the q = 0 case in the post, pressing the AGI button is favored when:

    p < x / (delta + x)

Solving the boundary for delta gives:

    delta = x / p - x

This script colors that break-even delta field and draws threshold contours on
log-scaled x and p axes.

Run from this folder with:

    python plot_xrisk_threshold.py

Output:

    xrisk_threshold_contours.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


HERE = Path(__file__).resolve().parent

DEFAULT_DELTAS = [0.0, 0.001, 0.005, 0.01, 0.02, 0.035, 0.05]
DEFAULT_X_MIN = 1e-5
DEFAULT_X_MAX = 1e-1
DEFAULT_P_MIN = 1e-3
DEFAULT_P_MAX = 1.0
DEFAULT_OUTPUT = HERE / "xrisk_threshold_contours.png"
DELTA = "\N{GREEK SMALL LETTER DELTA}"
COLOR_MIN_DELTA = 1e-4
COLOR_MAX_DELTA = 1e-1
COLOR_CENTER_DELTA = 0.02

DELTA_LABELS = {
    0.0: f"{DELTA} = 0% (no discounting)",
    0.001: f"{DELTA} = 0.1%",
    0.005: f"{DELTA} = 0.5%",
    0.01: f"{DELTA} = 1%",
    0.02: f"{DELTA} = 2%",
    0.035: f"{DELTA} = 3.5%",
    0.05: f"{DELTA} = 5%",
}

X_TICKS = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
P_TICKS = [1e-3, 1e-2, 1e-1, 1.0]
LABEL_X_POSITIONS = {
    0.001: 2.5e-5,
    0.005: 1.9e-4,
    0.01: 7.5e-4,
    0.02: 3e-3,
    0.035: 1.2e-2,
    0.05: 3e-2,
}


def discount_rate_field(
    x_grid: np.ndarray,
    p_grid: np.ndarray,
) -> np.ndarray:
    """Return the discount rate that makes each (x, p) point break even."""
    return x_grid / p_grid - x_grid


def format_delta(delta: float) -> str:
    for labeled_delta, label in DELTA_LABELS.items():
        if abs(delta - labeled_delta) < 1e-12:
            return label

    percent = 100 * delta
    if abs(percent - round(percent)) < 1e-12:
        percent_text = f"{round(percent):.0f}%"
    else:
        percent_text = f"{percent:g}%"
    return f"{DELTA} = {percent_text}"


def threshold_probability(x_value: float, delta: float) -> float:
    return x_value / (delta + x_value)


def label_positions(deltas: list[float]) -> list[tuple[float, float]]:
    positions = []
    for delta in deltas:
        x_value = LABEL_X_POSITIONS.get(delta)
        if x_value is not None:
            positions.append((x_value, threshold_probability(x_value, delta)))
    return positions


def fraction_tick_label(value: float, _position: int) -> str:
    if value <= 0:
        return ""
    if abs(value - 1.0) < 1e-12:
        return "100%"

    denominator = round(1 / value)
    if denominator > 1 and abs(value - 1 / denominator) < value * 1e-6:
        return f"1 in {denominator:,}"

    return f"{value:g}"


def draw_background(
    ax: plt.Axes,
    x_grid: np.ndarray,
    p_grid: np.ndarray,
    delta_grid: np.ndarray,
) -> None:
    color_values = np.clip(delta_grid, COLOR_MIN_DELTA, COLOR_MAX_DELTA)
    color_values = np.log10(color_values / COLOR_CENTER_DELTA)
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "pale_red_white_blue",
        ["#e8aaa5", "#ffffff", "#a8cce5"],
    )

    ax.pcolormesh(
        x_grid,
        p_grid,
        color_values,
        norm=mcolors.TwoSlopeNorm(vmin=-2.0, vcenter=0.0, vmax=1.0),
        cmap=cmap,
        shading="auto",
        alpha=0.34,
        rasterized=True,
    )


def draw_thresholds(
    ax: plt.Axes,
    x_grid: np.ndarray,
    p_grid: np.ndarray,
    delta_grid: np.ndarray,
    deltas: list[float],
) -> None:
    positive_deltas = sorted(delta for delta in deltas if delta > 0)
    if not positive_deltas:
        return

    contours = ax.contour(
        x_grid,
        p_grid,
        delta_grid,
        levels=positive_deltas,
        colors="black",
        linewidths=1.35,
    )
    contour_labels = {level: format_delta(level) for level in contours.levels}
    ax.clabel(
        contours,
        contours.levels,
        inline=True,
        inline_spacing=3,
        fmt=contour_labels,
        fontsize=9,
        colors="black",
        manual=label_positions(positive_deltas),
    )


def make_plot(
    deltas: list[float],
    x_min: float,
    x_max: float,
    p_min: float,
    p_max: float,
    show_reference: bool,
) -> plt.Figure:
    x_values = np.geomspace(x_min, x_max, 700)
    p_values = np.geomspace(p_min, p_max, 700)
    x_grid, p_grid = np.meshgrid(x_values, p_values)
    delta_grid = discount_rate_field(x_grid, p_grid)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(p_min, p_max)

    draw_background(ax, x_grid, p_grid, delta_grid)
    draw_thresholds(ax, x_grid, p_grid, delta_grid, deltas)

    has_zero_delta = any(abs(delta) < 1e-12 for delta in deltas)
    if has_zero_delta:
        ax.axhline(
            1.0,
            color="black",
            linestyle="--",
            linewidth=1.35,
            clip_on=False,
        )

    reference_x = 1 / 1300
    if show_reference and x_min <= reference_x <= x_max:
        ax.axvline(
            reference_x,
            color="#666666",
            linestyle=":",
            linewidth=1,
            alpha=0.45,
        )
        ax.text(
            reference_x,
            p_min * 1.2,
            "1/1300 per year",
            rotation=90,
            va="bottom",
            ha="right",
            fontsize=9,
            color="#444444",
        )

    ax.set_xlabel("X: non-AI existential risk per year (which AGI can prevent)")
    ax.set_ylabel("P: probability AGI instantly destroys humanity")
    ax.set_title("AGI Existential Risk Tradeoffs")
    ax.xaxis.set_major_locator(ticker.FixedLocator(X_TICKS))
    ax.yaxis.set_major_locator(ticker.FixedLocator(P_TICKS))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(fraction_tick_label))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(fraction_tick_label))
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=10, subs=range(2, 10)))
    ax.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=range(2, 10)))
    ax.xaxis.set_minor_formatter(ticker.NullFormatter())
    ax.yaxis.set_minor_formatter(ticker.NullFormatter())
    ax.grid(True, which="major", alpha=0.28)
    ax.grid(True, which="minor", alpha=0.12)
    ax.spines["top"].set_visible(False)

    fig.tight_layout()

    if has_zero_delta:
        ax.text(
            x_min * 1.08,
            0.9,
            format_delta(0.0),
            color="black",
            fontsize=9,
            va="top",
        )

    return fig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot xrisk threshold contours p = x / (delta + x)."
    )
    parser.add_argument(
        "--deltas",
        type=float,
        nargs="+",
        default=DEFAULT_DELTAS,
        help="Discount rates to plot, e.g. --deltas 0 0.02 0.035.",
    )
    parser.add_argument("--x-min", type=float, default=DEFAULT_X_MIN)
    parser.add_argument("--x-max", type=float, default=DEFAULT_X_MAX)
    parser.add_argument("--p-min", type=float, default=DEFAULT_P_MIN)
    parser.add_argument("--p-max", type=float, default=DEFAULT_P_MAX)
    parser.add_argument(
        "--reference",
        action="store_true",
        dest="show_reference",
        help="Show the 1/1300 per year reference line.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output PNG path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    fig = make_plot(
        args.deltas,
        args.x_min,
        args.x_max,
        args.p_min,
        args.p_max,
        args.show_reference,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=200)
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
