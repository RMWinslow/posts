"""
Spaghetti plot of commodity purchasing power over time.

Y-axis (log scale): tons of commodity purchasable per GDP-per-capita.
X-axis: year (1929-2022).
Most commodities in light gray; a few interesting ones highlighted and labeled.

Outputs: gg_spaghetti.png, gg_indexed.png
Run with: python gg_plot.py
"""

import sys
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# Commodities to highlight with color and label.
HIGHLIGHTS = {
    "gold":           "#DAA520",
    "silver":         "#A0A0A0",
    "diamond":        "#40C0E0",
    "copper":         "#B87333",
    "sulfur":         "#E8E020",
    "aluminum":       "#6090C0",
    "gemstones":      "#E040E0",
    "platinum":       "#80A0B0",
    "salt":           "#F0A0A0",
}

INDEX_YEAR = 1950  # Base year for the indexed plot.


def load_wide():
    path = os.path.join(HERE, "gg_timeseries_wide.csv")
    return pd.read_csv(path, index_col=0)


def plot_spaghetti(wide):
    """Absolute purchasing power (tons per GDP per capita) over time."""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Background: all commodities in light gray.
    for col in wide.columns:
        if col not in HIGHLIGHTS:
            series = wide[col].dropna()
            ax.plot(series.index, series.values,
                    color="#D0D0D0", linewidth=0.6, alpha=0.7)

    # Foreground: highlighted commodities.
    for name, color in HIGHLIGHTS.items():
        if name not in wide.columns:
            continue
        series = wide[name].dropna()
        ax.plot(series.index, series.values,
                color=color, linewidth=2, label=name)
        # Label at the right end of each line.
        if len(series) > 0:
            ax.annotate(name,
                        xy=(series.index[-1], series.values[-1]),
                        fontsize=8, color=color,
                        xytext=(5, 0), textcoords="offset points",
                        va="center")

    ax.set_yscale("log")
    ax.set_xlabel("Year")
    ax.set_ylabel("Tons purchasable per GDP per capita")
    ax.set_title("Commodity Purchasing Power, 1929\u20132022\n"
                 "(How many tons of each commodity could one GDP-per-capita buy?)")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_indexed(wide, base_year=INDEX_YEAR):
    """Purchasing power indexed to 100 at base_year. Shows relative growth."""
    # Only include commodities that have data at the base year.
    base_row = wide.loc[base_year] if base_year in wide.index else None
    if base_row is None:
        print(f"No data for base year {base_year}", file=sys.stderr)
        return None

    usable = base_row.dropna()
    usable = usable[usable > 0]
    indexed = wide[usable.index].div(usable) * 100

    fig, ax = plt.subplots(figsize=(12, 7))

    for col in indexed.columns:
        if col not in HIGHLIGHTS:
            series = indexed[col].dropna()
            ax.plot(series.index, series.values,
                    color="#D0D0D0", linewidth=0.6, alpha=0.7)

    for name, color in HIGHLIGHTS.items():
        if name not in indexed.columns:
            continue
        series = indexed[name].dropna()
        ax.plot(series.index, series.values,
                color=color, linewidth=2, label=name)
        if len(series) > 0:
            ax.annotate(name,
                        xy=(series.index[-1], series.values[-1]),
                        fontsize=8, color=color,
                        xytext=(5, 0), textcoords="offset points",
                        va="center")

    ax.set_yscale("log")
    ax.axhline(100, color="black", linewidth=0.8, linestyle="--", alpha=0.5)
    ax.set_xlabel("Year")
    ax.set_ylabel(f"Purchasing power (indexed: {base_year} = 100)")
    ax.set_title(f"Commodity Purchasing Power Growth (indexed to {base_year})\n"
                 "Above 100 = more affordable than in "
                 f"{base_year}; below 100 = less affordable")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    wide = load_wide()
    print(f"Loaded {len(wide.columns)} commodities, "
          f"years {wide.index.min()}-{wide.index.max()}", file=sys.stderr)

    fig1 = plot_spaghetti(wide)
    path1 = os.path.join(HERE, "gg_spaghetti.png")
    fig1.savefig(path1, dpi=150)
    print(f"Saved {path1}", file=sys.stderr)

    fig2 = plot_indexed(wide)
    if fig2:
        path2 = os.path.join(HERE, "gg_indexed.png")
        fig2.savefig(path2, dpi=150)
        print(f"Saved {path2}", file=sys.stderr)
