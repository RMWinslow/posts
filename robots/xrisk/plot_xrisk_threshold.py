"""
Plot the AGI-button threshold from ../xrisk.md.

For the q = 0 case in the post, pressing the AGI button is favored when:

    p < x / (delta + x)

This script plots that boundary for delta = 2%, with x on a log scale.

Run from this folder with:

    python plot_xrisk_threshold.py

Output:

    xrisk_threshold_delta_2pct.png
"""

#%%

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent

DEFAULT_DELTA = 0.02
DEFAULT_X_MIN = 1e-6
DEFAULT_X_MAX = 1e-2
DEFAULT_OUTPUT = HERE / "xrisk_threshold_delta_2pct.png"


def threshold_probability(x_values: np.ndarray, delta: float) -> np.ndarray:
    """Return the q = 0 threshold p = x / (delta + x)."""
    return x_values / (delta + x_values)


def make_plot(delta: float, x_min: float, x_max: float) -> plt.Figure:
    x_values = np.geomspace(x_min, x_max, 500)
    p_values = threshold_probability(x_values, delta)

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.fill_between(
        x_values,
        0,
        p_values,
        color="#7AA6C2",
        alpha=0.25,
        label="Turn on AGI",
    )
    ax.fill_between(
        x_values,
        p_values,
        1,
        color="#D98982",
        alpha=0.18,
        label="Do not turn on AGI",
    )
    ax.plot(
        x_values,
        p_values,
        color="#1D5F82",
        linewidth=2.5,
        label=f"Threshold, delta = {delta:.0%}",
    )

    reference_x = 1 / 1300
    if x_min <= reference_x <= x_max:
        reference_p = threshold_probability(np.array([reference_x]), delta)[0]
        ax.scatter(
            [reference_x],
            [reference_p],
            color="#111111",
            s=35,
            zorder=3,
        )
        ax.annotate(
            "1/1300 per year -> 3.7%",
            xy=(reference_x, reference_p),
            xytext=(10, 12),
            textcoords="offset points",
            fontsize=9,
            color="#111111",
        )

    ax.set_xscale("log")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0, 1)
    ax.set_xlabel("X: non-AI existential risk per year")
    ax.set_ylabel("P: probability AGI instantly destroys humanity")
    ax.set_title("AGI Button Threshold")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(loc="upper left")

    fig.tight_layout()
    return fig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot the xrisk threshold p = x / (delta + x)."
    )
    parser.add_argument("--delta", type=float, default=DEFAULT_DELTA)
    parser.add_argument("--x-min", type=float, default=DEFAULT_X_MIN)
    parser.add_argument("--x-max", type=float, default=DEFAULT_X_MAX)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output PNG path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    fig = make_plot(args.delta, args.x_min, args.x_max)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=200)
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()

# %%
