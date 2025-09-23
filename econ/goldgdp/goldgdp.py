#%%
# Open and read data from ds140-gold-2022.xlsx
# or similar files.
# In each one, the data table headers are on row 5
# And the year column is always the first column
import pandas as pd
import os

YEAR = 2019

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
    results = []
    files = [f for f in os.listdir('.') if f.endswith('.xlsx')]
    for f in files:
        label = f.split('-')[1]
        try:
            results.append((label, get_commodity_price(f, year)))
        except Exception as e:
            continue
    return results


get_all_results_by_year(YEAR)

# %%
