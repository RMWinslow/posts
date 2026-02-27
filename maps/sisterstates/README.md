# US State – Chinese Province Sister Relationships: Map Data Package

## Overview

This package contains research data on confirmed **sister state/province** relationships between US states and Chinese provinces. The goal is to produce a **QGIS map** showing Chinese province boundaries colored/labeled by their US sister state partners.

## Files

| File | Format | Description |
|------|--------|-------------|
| `pairings.json` | JSON | Full structured data with all 23 pairings, metadata, rationales, and join fields |
| `pairings.csv` | CSV | Flat table version for easy import into QGIS or pandas |
| `README.md` | Markdown | This documentation file |

## Data Structure

Each pairing record contains:

- **`us_state`** / **`us_abbr`** – Full name and 2-letter abbreviation of US state
- **`cn_province`** – English name of Chinese province/municipality
- **`cn_province_chinese`** – Chinese characters (e.g. 湖北省)
- **`cn_join_field_adm1`** – **Key field for joining to Natural Earth shapefile** (see below)
- **`year_established`** – Year the agreement was signed (null for Washington-Sichuan)
- **`type`** – Either `sister_state` or `friendship_agreement`
- **`rationale`** – Brief explanation of why the pairing was formed

## Critical: This is NOT a 1:1 Mapping

Some provinces have multiple US partners and vice versa. The map must handle this:

### Chinese provinces with multiple US partners:
| Province | US Partners |
|----------|-------------|
| **Guangdong** | Massachusetts (1983), California (2014), Michigan (2016) |
| **Zhejiang** | New Jersey (1981), Indiana (1987) |
| **Fujian** | Oregon (1984), Pennsylvania (2009) |
| **Sichuan** | Michigan (1982), Washington (friendship only) |

### US states with multiple Chinese partners:
| State | Chinese Partners |
|-------|-----------------|
| **Michigan** | Sichuan (1982), Guangdong (2016) |
| **Oregon** | Fujian (1984), Tianjin (2014) |

### Visualization suggestion for multi-partner provinces:
- Use the **earliest** pairing's color as the province fill
- Add **multiple labels** (e.g., "MA / CA / MI" for Guangdong)
- Or use **striped/hatched fills** to show multiple relationships
- The `pairings.json` groups pairings per-record (one row per agreement), so you'll need to aggregate by `cn_province` to get all US partners for a given province

## Joining to Natural Earth Shapefile

### Recommended shapefile
**Natural Earth Admin 1 – States/Provinces** (1:10m or 1:50m scale):
- Download: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/
- File: `ne_10m_admin_1_states_provinces.shp` (or the 50m version)

### Join strategy

The Natural Earth shapefile has these relevant attribute columns:

| NE Column | Example Value | Notes |
|-----------|---------------|-------|
| `name` | `"Hubei"` | English name — **primary join field** |
| `name_zh` | `"湖北"` | Chinese name (short form, no 省/市 suffix) |
| `admin` | `"China"` | Country — filter to `admin = 'China'` first |
| `adm1_code` | `"CHN-1177"` | Unique code |
| `iso_3166_2` | `"CN-42"` | ISO code for Hubei |

**Recommended join:**

```
Filter: admin = 'China'
Join: ne_shapefile.name = pairings.cn_join_field_adm1
```

The `cn_join_field_adm1` field in the data files is specifically formatted to match Natural Earth's `name` column.

### Potential name mismatches to watch for

| Our Data | Natural Earth `name` | Issue |
|----------|---------------------|-------|
| `Shaanxi` | May appear as `Shaanxi` or `Shanxi` | Double-A spelling. NE usually uses `Shaanxi` correctly. Verify. |
| `Inner Mongolia` | `Inner Mongol` or `Nei Mongol` | NE sometimes truncates or uses Chinese romanization |
| `Tibet` | `Xizang` or `Tibet` | NE may use either name |
| `Tianjin` | `Tianjin` | Municipality, not province — should still be in admin-1 |

If the join misses any provinces, try fuzzy matching or check the `name_en`, `name_alt`, or `name_zh` columns in Natural Earth.

## Suggested Map Design

### China layer (province polygons)
- **Paired provinces**: Filled with a distinct color per pairing, labeled with US state abbreviation(s)
- **Unpaired provinces**: Light gray or transparent fill, thin border
- **Multi-partner provinces**: Combined label (e.g., "MA/CA/MI"), possibly hatched fill or distinct border

### Color palette used in earlier web visualizations
These hex colors were chosen for the web version and could be reused:

```
Hubei/OH:        #E63946  (red)
Anhui/MD:        #457B9D  (steel blue)
Zhejiang/NJ+IN:  #2A9D8F  (teal)
Henan/KS:        #E9C46A  (gold)
Shaanxi/MN:      #F4A261  (orange)
Sichuan/MI+WA:   #264653  (dark teal)
Heilongjiang/WI: #6A994E  (olive green)
Liaoning/IL:     #BC6C25  (brown)
Guangdong/MA+CA+MI: #9B2226 (dark red)
Hebei/IA:        #AE2012  (rust)
Fujian/OR+PA:    #005F73  (dark cyan)
Shandong/CT:     #0A9396  (cyan)
Gansu/OK:        #BB3E03  (burnt orange)
Shanxi/ID:       #CA6702  (amber)
Jiangsu/NY:      #EE9B00  (yellow-orange)
Jilin/ME:        #3D5A80  (slate blue)
Hainan/HI:       #E07A5F  (salmon)
Tianjin/OR:      #8338EC  (purple)
```

### Labels
- Inside each paired province: US state abbreviation(s) in white, bold
- Province name as secondary label or on hover/tooltip

### Optional additions
- Small inset showing which US states are paired (US map in corner)
- Year labels or a timeline legend
- Title: "China's Provinces & Their US Sister States"

## Context & Sources

- **Total ~50 pairings** reportedly exist as of 2023, but no comprehensive public database was found
- **23 pairings confirmed** through official sources during this research
- The program began in 1979 (Ohio-Hubei) coinciding with US-China diplomatic normalization
- Sources: Chinese consulate websites, state government international relations offices, CPAFFC records, news archives
- Recent political context: Indiana banned new China sister city partnerships (2024), Texas followed (2025)

## Quick Start for Claude Code Agent

```python
import geopandas as gpd
import pandas as pd
import json

# Load Natural Earth admin-1
china = gpd.read_file("ne_10m_admin_1_states_provinces.shp")
china = china[china["admin"] == "China"]

# Load pairings
with open("pairings.json") as f:
    data = json.load(f)
pairings_df = pd.DataFrame(data["pairings"])

# Aggregate US partners per province
grouped = pairings_df.groupby("cn_join_field_adm1").agg({
    "us_abbr": lambda x: "/".join(x),
    "us_state": lambda x: ", ".join(x),
    "year_established": "min",
    "rationale": "first"
}).reset_index()

# Join
merged = china.merge(grouped, left_on="name", right_on="cn_join_field_adm1", how="left")

# Now style and export in QGIS or save as GeoPackage
merged.to_file("china_sister_states.gpkg", driver="GPKG")
```
