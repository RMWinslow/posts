"""
Shared data loader for the gold/GDP commodity analysis.

Reads USGS mineral commodity spreadsheets and FRED GDP data.
Every other gg_* script imports this module.
"""

import os
import re
import pandas as pd

# Paths are relative to this file's directory.
HERE = os.path.dirname(os.path.abspath(__file__))
USGS_DIR = os.path.join(HERE, "usgs")
GDPPC_CSV = os.path.join(HERE, "A939RC0A052NBEA.csv")
GDPA_CSV = os.path.join(HERE, "GDPA.csv")


def find_unit_value_column(columns):
    """Find the nominal unit-value column despite inconsistent whitespace.

    USGS files use variants like 'Unit value ($/t)', 'Unit value  ($/t)',
    'Unit value $/t', 'Unit value     $/t', 'Unit value ($/t) ', etc.
    We want the nominal (not inflation-adjusted '98$/t') column.
    """
    candidates = []
    for col in columns:
        normalized = re.sub(r"\s+", " ", str(col).strip().lower())
        if "unit value" not in normalized:
            continue
        # Skip the constant-dollar (1998-adjusted) column.
        if "98" in normalized:
            continue
        candidates.append(col)

    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        # Prefer the one with $/t in it.
        for c in candidates:
            if "$/t" in c:
                return c
        return candidates[0]
    return None


def find_real_unit_value_column(columns):
    """Find the 1998-constant-dollar unit-value column (the '98$/t' one)."""
    for col in columns:
        normalized = re.sub(r"\s+", " ", str(col).strip().lower())
        if "unit value" in normalized and "98" in normalized:
            return col
    return None


def commodity_name_from_filename(filename):
    """Extract a human-readable name from 'ds140-gold-2022.xlsx'."""
    base = os.path.basename(filename)
    # Strip prefix and -YYYY.xlsx suffix.
    name = re.sub(r"^ds140-", "", base)
    name = re.sub(r"-?\d{4}(_\d)?\.xlsx$", "", name)
    name = re.sub(r"\.xlsx$", "", name)
    return name.strip("-_ ")


def load_commodity(filepath):
    """Read one USGS xlsx file; return a clean DataFrame or None.

    Returns columns: [year, unit_value_nominal]
    Rows with missing or non-numeric unit values are dropped.
    """
    df = pd.read_excel(filepath, skiprows=4)

    # Some files (like abran.xlsx) have a shifted header row.
    if "Year" not in df.columns:
        df = pd.read_excel(filepath, skiprows=5)
    if "Year" not in df.columns:
        return None

    col = find_unit_value_column(df.columns)
    if col is None:
        return None

    real_col = find_real_unit_value_column(df.columns)

    out = pd.DataFrame()
    out["year"] = pd.to_numeric(df["Year"], errors="coerce")
    out["unit_value_nominal"] = pd.to_numeric(df[col], errors="coerce")
    if real_col is not None:
        out["unit_value_real"] = pd.to_numeric(df[real_col], errors="coerce")
    out = out.dropna(subset=["year", "unit_value_nominal"])
    out["year"] = out["year"].astype(int)
    return out.reset_index(drop=True)


def load_all_commodities(usgs_dir=USGS_DIR):
    """Load every USGS spreadsheet that has a unit-value column.

    Returns {commodity_name: DataFrame} with duplicates skipped.
    """
    commodities = {}
    for f in sorted(os.listdir(usgs_dir)):
        if not f.endswith(".xlsx"):
            continue
        # Skip obvious duplicates like 'ds140-iron-steel-2021 (1).xlsx'.
        if " (" in f:
            continue

        name = commodity_name_from_filename(f)
        df = load_commodity(os.path.join(usgs_dir, f))
        if df is not None and len(df) > 0:
            commodities[name] = df
    return commodities


def load_gdp_per_capita(path=GDPPC_CSV):
    """Read the FRED GDP-per-capita CSV. Returns columns [year, gdppc]."""
    df = pd.read_csv(path)
    col = [c for c in df.columns if c != "observation_date"][0]
    out = pd.DataFrame()
    out["year"] = pd.to_datetime(df["observation_date"]).dt.year
    out["gdppc"] = pd.to_numeric(df[col], errors="coerce")
    return out.dropna().reset_index(drop=True)


def load_nominal_gdp(path=GDPA_CSV):
    """Read the FRED nominal GDP CSV. Returns columns [year, gdp]."""
    df = pd.read_csv(path)
    col = [c for c in df.columns if c != "observation_date"][0]
    out = pd.DataFrame()
    out["year"] = pd.to_datetime(df["observation_date"]).dt.year
    out["gdp"] = pd.to_numeric(df[col], errors="coerce")
    return out.dropna().reset_index(drop=True)


def extract_cpi(commodities):
    """Back-calculate CPI from the ratio of nominal to real (1998$) prices.

    The USGS deflates nominal prices using CPI-U with 1998=100.
    For each year, we take the median ratio across all commodities
    that have both columns, which cancels out commodity-specific noise.
    """
    ratios_by_year = {}
    for name, df in commodities.items():
        if "unit_value_real" not in df.columns:
            continue
        both = df.dropna(subset=["unit_value_nominal", "unit_value_real"])
        both = both[both["unit_value_real"] > 0]
        for _, row in both.iterrows():
            year = int(row["year"])
            ratio = row["unit_value_nominal"] / row["unit_value_real"]
            ratios_by_year.setdefault(year, []).append(ratio)

    rows = []
    for year in sorted(ratios_by_year):
        vals = ratios_by_year[year]
        rows.append({"year": year, "cpi_index": pd.Series(vals).median()})
    return pd.DataFrame(rows)
