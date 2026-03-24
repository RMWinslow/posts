"""
Plot commodity price changes since 1950, with CPI and nominal GDP as reference.

Each commodity's nominal price is indexed to its 1950 value (1950 = 1).
Reference lines show how CPI and nominal GDP per capita grew over the
same period, so you can see which commodities outpaced or lagged inflation
and income growth.

Output: gg_price_changes.png
Run with: python gg_plot_prices.py
"""

import sys
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from gg_loader import (
    load_all_commodities, load_gdp_per_capita, load_nominal_gdp,
    extract_cpi, HERE,
)

BASE_YEAR = 1950

HIGHLIGHTS = {
    "gold":      "#DAA520",
    "silver":    "#A0A0A0",
    "diamond":   "#40C0E0",
    "copper":    "#B87333",
    "sulfur":    "#E8E020",
    "aluminum":  "#6090C0",
    "gemstones": "#E040E0",
    "platinum":  "#80A0B0",
    "salt":      "#F0A0A0",
}


def index_to_base(series, years, base_year):
    """Divide all values by the base-year value, so base_year = 1."""
    base_mask = years == base_year
    if not base_mask.any():
        return None, None
    base_val = series[base_mask].values[0]
    if base_val <= 0:
        return None, None
    return years[years >= base_year], (series / base_val)[years >= base_year]


def build_price_index(commodities, base_year):
    """For each commodity, index nominal price to base_year = 1."""
    indexed = {}
    for name, df in commodities.items():
        yrs, vals = index_to_base(
            df["unit_value_nominal"], df["year"], base_year
        )
        if yrs is not None and len(yrs) > 1:
            indexed[name] = pd.DataFrame({"year": yrs.values, "price_idx": vals.values})
    return indexed


def main():
    print("Loading data...", file=sys.stderr)
    commodities = load_all_commodities()
    gdppc = load_gdp_per_capita()
    gdp = load_nominal_gdp()
    cpi = extract_cpi(commodities)

    # Index CPI and GDP per capita to base year.
    cpi_base = cpi.loc[cpi.year == BASE_YEAR, "cpi_index"].values[0]
    cpi["cpi_idx"] = cpi["cpi_index"] / cpi_base
    cpi = cpi[cpi.year >= BASE_YEAR]

    gdppc_base = gdppc.loc[gdppc.year == BASE_YEAR, "gdppc"].values[0]
    gdppc["gdppc_idx"] = gdppc["gdppc"] / gdppc_base
    gdppc = gdppc[gdppc.year >= BASE_YEAR]

    indexed = build_price_index(commodities, BASE_YEAR)
    print(f"{len(indexed)} commodities with 1950 baseline.", file=sys.stderr)

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(12, 7))

    # Background: all commodity price trajectories.
    for name, df in indexed.items():
        if name not in HIGHLIGHTS:
            ax.plot(df["year"], df["price_idx"],
                    color="#D0D0D0", linewidth=0.5, alpha=0.6)

    # Highlighted commodities.
    for name, color in HIGHLIGHTS.items():
        if name not in indexed:
            continue
        df = indexed[name]
        ax.plot(df["year"], df["price_idx"],
                color=color, linewidth=1.8, label=name)
        ax.annotate(name,
                    xy=(df["year"].iloc[-1], df["price_idx"].iloc[-1]),
                    fontsize=8, color=color,
                    xytext=(5, 0), textcoords="offset points", va="center")

    # Reference lines: CPI and GDP per capita.
    ax.plot(cpi["year"], cpi["cpi_idx"],
            color="red", linewidth=2.5, linestyle="--", label="CPI (overall prices)")
    ax.annotate("CPI",
                xy=(cpi["year"].iloc[-1], cpi["cpi_idx"].iloc[-1]),
                fontsize=9, fontweight="bold", color="red",
                xytext=(5, 0), textcoords="offset points", va="center")

    ax.plot(gdppc["year"], gdppc["gdppc_idx"],
            color="darkblue", linewidth=2.5, linestyle="--",
            label="Nominal GDP per capita")
    ax.annotate("GDP/cap",
                xy=(gdppc["year"].iloc[-1], gdppc["gdppc_idx"].iloc[-1]),
                fontsize=9, fontweight="bold", color="darkblue",
                xytext=(5, 0), textcoords="offset points", va="center")

    ax.set_yscale("log")
    ax.axhline(1, color="black", linewidth=0.8, linestyle=":", alpha=0.4)
    ax.set_xlabel("Year")
    ax.set_ylabel(f"Price index ({BASE_YEAR} = 1)")
    ax.set_title(
        f"Commodity Price Changes Since {BASE_YEAR}\n"
        f"Below CPI = got cheaper in real terms; "
        f"below GDP/cap = became more affordable"
    )
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    outpath = os.path.join(HERE, "gg_price_changes.png")
    fig.savefig(outpath, dpi=150)
    print(f"Saved {outpath}", file=sys.stderr)


if __name__ == "__main__":
    main()
