#%%
# Open and read data from ds140-gold-2022.xlsx
# or similar files.
# In each one, the data table headers are on row 5
# And the year column is always the first column
import pandas as pd
import os

def get_commodity_price(filename, year, column="Unit value ($/t)"):
    import pandas as pd
    df = pd.read_excel(filename, skiprows=4)
    row = df[df['Year'] == year]
    # if row.empty:
    #     raise ValueError(f"Year {year} not found in the data.")
    # if column not in df.columns:
    #     raise ValueError(f"Column '{column}' not found in the data.")
    value = row.iloc[0][column]
    return value


def get_all_results_by_year(year, column="Unit value ($/t)"):
    results = dict()
    files = [f for f in os.listdir('.') if f.endswith('.xlsx')]
    for f in files:
        label = f[6:-10] #cut off -yyyy.xlsx at end and ds140- at start
        try:
            results[label] = get_commodity_price(f, year)
        except Exception as e:
            continue
    return results


results1950 = get_all_results_by_year(1950)
results2020 = get_all_results_by_year(2020)
results2019 = get_all_results_by_year(2019)



#%%
# Manually input GDP values for 1950 and 2020
# (Taken from GDPA.csv)
gdp1950 = 299.827 * 1_000_000_000 # Interestingly, AI said "222.89  # in billions of dollars"
gdp2020 = 21354.105  * 1_000_000_000 # AI guess was 21_433.226
gdp2019 = 21539.982  * 1_000_000_000 # AI guess was 21_433.226 (just copied 2020)

# and GDP per capita (A939RC0A052NBEA.csv)
gdppc1950 = 1977 # AI guess was "2_074.0 # AI guess was 1_680.0"
gdppc2020 = 64414 # "AI guess was "65_297.0 # AI guess was 65_297.0"""
gdppc2019 = 65171 # "AI guess was "65_297.0 # AI guess was 65_297.0""

# personal income per capita (A792RC0A052NBEA.csv) AI guess: (A229RX0A052NBEA.csv)
pipc1950 = 1541
pipc2020 = 59160
pipc2019 = 55560




# %%
# iterate through interesection of keys in both dictionaries
common_keys = set(results1950.keys()).intersection(set(results2020.keys()))
stats_list = []
for k in common_keys:
    if k in results2020:
        stats = dict()
        stats['material'] = k
        stats['p1950 ($/t)'] = results1950[k]
        stats['p2020 ($/t)'] = results2020[k]
        # if either is non-numeric, skip
        try:
            stats['p_ratio'] = results2020[k] / results1950[k]
        except Exception as e:
            continue
        # skip if ratio is nan
        if pd.isna(stats['p_ratio']): 
            continue
        stats['gdppc1950_tons'] = gdppc1950 / results1950[k]
        stats['gdppc2020_tons'] = gdppc2020 / results2020[k]
        gdppc_ratio = gdppc2020 / gdppc1950
        stats['gdppc_tons_ratio'] = stats['gdppc2020_tons'] / stats['gdppc1950_tons']
        # stats['gdppc_tons_ratio2'] = gdppc_ratio / stats['p_ratio'] 
        
        # stats['pipc1950_tons'] = pipc1950 / results1950[k]
        # stats['pipc2020_tons'] = pipc2020 / results2020[k]
        # stats['pipc_tons_ratio'] = stats['pipc2020_tons'] / stats['pipc1950_tons']
        print(stats)
        stats_list.append(stats)

df = pd.DataFrame(stats_list)

# sort by gdpcc_tons_ratio descending
df = df.sort_values(by='gdppc_tons_ratio', ascending=False)
# df.sort_values(by='pipc_tons_ratio', ascending=False)


with pd.option_context('display.precision', 2, 'display.max_rows', 100,):
    display(df)


# %%
