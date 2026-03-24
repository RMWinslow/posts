"""
Generate markdown tables comparing commodity purchasing power across two years.

Outputs to stdout and to gg_tables_output.md.
Run with: python gg_tables.py [start_year] [end_year]
Defaults: 1950 2020
"""

import sys
import pandas as pd
from gg_loader import load_all_commodities, load_gdp_per_capita


def purchasing_power_table(commodities, gdp, year_a, year_b):
    """Build a DataFrame of purchasing-power ratios between two years.

    For each commodity, computes how many tons one GDP-per-capita could buy
    in each year, and the ratio (year_b / year_a).
    """
    gdppc_a = gdp.loc[gdp.year == year_a, "gdppc"].values
    gdppc_b = gdp.loc[gdp.year == year_b, "gdppc"].values
    if len(gdppc_a) == 0 or len(gdppc_b) == 0:
        print(f"No GDP data for {year_a} or {year_b}", file=sys.stderr)
        return pd.DataFrame()
    gdppc_a, gdppc_b = float(gdppc_a[0]), float(gdppc_b[0])

    rows = []
    for name, df in commodities.items():
        price_a = df.loc[df.year == year_a, "unit_value_nominal"]
        price_b = df.loc[df.year == year_b, "unit_value_nominal"]
        if price_a.empty or price_b.empty:
            continue
        pa, pb = float(price_a.values[0]), float(price_b.values[0])
        if pa == 0 or pb == 0:
            continue
        rows.append({
            "commodity": name,
            f"price_{year_a}": pa,
            f"price_{year_b}": pb,
            "price_growth": pb / pa,
            f"tons_per_gdppc_{year_a}": gdppc_a / pa,
            f"tons_per_gdppc_{year_b}": gdppc_b / pb,
            "purchasing_power_change": (gdppc_b / pb) / (gdppc_a / pa),
        })

    result = pd.DataFrame(rows)
    result = result.sort_values("purchasing_power_change", ascending=False)
    return result.reset_index(drop=True)


def format_number(x):
    """Format numbers readably: big numbers get commas, small get decimals."""
    if abs(x) >= 1000:
        return f"{x:,.0f}"
    if abs(x) >= 10:
        return f"{x:.1f}"
    if abs(x) >= 1:
        return f"{x:.2f}"
    return f"{x:.4f}"


def to_markdown(df, year_a, year_b, title, subset=None):
    """Render a purchasing-power DataFrame as a markdown table."""
    if subset is not None:
        df = df.head(subset) if subset > 0 else df.tail(-subset)

    lines = [f"### {title}\n"]
    lines.append(f"| Commodity | Price {year_a} ($/t) | Price {year_b} ($/t) "
                 f"| Price growth | Purchasing power change |")
    lines.append("|---|---:|---:|---:|---:|")

    for _, row in df.iterrows():
        lines.append(
            f"| {row['commodity']} "
            f"| {format_number(row[f'price_{year_a}'])} "
            f"| {format_number(row[f'price_{year_b}'])} "
            f"| {row['price_growth']:.1f}x "
            f"| {row['purchasing_power_change']:.1f}x |"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    year_a = int(sys.argv[1]) if len(sys.argv) > 1 else 1950
    year_b = int(sys.argv[2]) if len(sys.argv) > 2 else 2020

    print(f"Loading data...", file=sys.stderr)
    commodities = load_all_commodities()
    gdp = load_gdp_per_capita()
    gdppc_a = float(gdp.loc[gdp.year == year_a, "gdppc"].values[0])
    gdppc_b = float(gdp.loc[gdp.year == year_b, "gdppc"].values[0])

    df = purchasing_power_table(commodities, gdp, year_a, year_b)
    print(f"{len(df)} commodities with data for both {year_a} and {year_b}.",
          file=sys.stderr)
    print(f"GDP per capita: ${gdppc_a:,.0f} ({year_a}) -> "
          f"${gdppc_b:,.0f} ({year_b}) = {gdppc_b/gdppc_a:.1f}x growth.\n",
          file=sys.stderr)

    sections = [
        to_markdown(df, year_a, year_b,
                    f"All commodities ({year_a} vs {year_b})"),
        to_markdown(df, year_a, year_b,
                    "Top 10: biggest purchasing power gains", subset=10),
        to_markdown(df, year_a, year_b,
                    "Bottom 10: smallest gains (or losses)", subset=-10),
    ]
    output = "\n\n".join(sections)
    print(output)

    outpath = "gg_tables_output.md"
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(output + "\n")
    print(f"\nSaved to {outpath}", file=sys.stderr)
