"""
Build year-by-year purchasing power time series for all commodities.

For each commodity and year, computes: GDP per capita / price per ton
= how many tons of that commodity one person's GDP could buy.

Outputs:
  gg_timeseries.csv      (long format: year, commodity, tons_per_gdppc)
  gg_timeseries_wide.csv (wide format: years as rows, commodities as columns)

Run with: python gg_timeseries.py
"""

import sys
import pandas as pd
from gg_loader import load_all_commodities, load_gdp_per_capita, HERE
import os


def build_timeseries(commodities, gdp):
    """Merge all commodity prices with GDP, compute purchasing power."""
    rows = []
    for name, df in commodities.items():
        merged = df.merge(gdp, on="year", how="inner")
        merged["tons_per_gdppc"] = merged["gdppc"] / merged["unit_value_nominal"]
        for _, r in merged.iterrows():
            rows.append({
                "year": int(r["year"]),
                "commodity": name,
                "tons_per_gdppc": r["tons_per_gdppc"],
                "unit_value_nominal": r["unit_value_nominal"],
                "gdppc": r["gdppc"],
            })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print("Loading data...", file=sys.stderr)
    commodities = load_all_commodities()
    gdp = load_gdp_per_capita()

    print(f"Building time series for {len(commodities)} commodities...",
          file=sys.stderr)
    ts = build_timeseries(commodities, gdp)
    print(f"Total rows: {len(ts)} "
          f"(years {ts.year.min()}-{ts.year.max()})", file=sys.stderr)

    # Long format.
    long_path = os.path.join(HERE, "gg_timeseries.csv")
    ts.to_csv(long_path, index=False)
    print(f"Saved long format: {long_path}", file=sys.stderr)

    # Wide format (just the purchasing power ratio).
    # Some commodities may have duplicate year entries; take the mean.
    wide = ts.pivot_table(
        index="year", columns="commodity",
        values="tons_per_gdppc", aggfunc="mean",
    )
    wide = wide.sort_index()
    wide_path = os.path.join(HERE, "gg_timeseries_wide.csv")
    wide.to_csv(wide_path)
    print(f"Saved wide format: {wide_path}", file=sys.stderr)
