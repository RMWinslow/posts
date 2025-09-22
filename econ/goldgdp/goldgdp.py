#%%
# Open and read data from ds140-gold-2022.xlsx
# or similar files.
# In each one, the data table headers are on row 5
# And the year column is always the first column
import pandas as pd

def get_commodity_price(filename, year, column="Unit value ($/t)"):
    import pandas as pd

    # Read the Excel file, skipping the first 4 rows
    df = pd.read_excel(filename, skiprows=4)

    # Display the first few rows of the dataframe to understand its structure
    print(df.head())

    # Assuming the data table ends before any citation data,
    # we can drop rows with NaN values in a specific column (e.g., 'Year')
    df = df.dropna(subset=['Year'])

    # Reset index after dropping rows
    df = df.reset_index(drop=True)

    # Find the row corresponding to the specified year
    row = df[df['Year'] == year]

    if row.empty:
        raise ValueError(f"Year {year} not found in the data.")

    # Extract the value from the specified column
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in the data.")

    value = row.iloc[0][column]

    return value


get_commodity_price('ds140-gold-2022.xlsx',2020)








#%%
def get_commodity_data(filename):
    import pandas as pd

    # Read the Excel file, skipping the first 4 rows
    df = pd.read_excel(filename, skiprows=4)

    # Display the first few rows of the dataframe to understand its structure
    print(df.head())

    # Assuming the data table ends before any citation data,
    # we can drop rows with NaN values in a specific column (e.g., 'Year')
    df = df.dropna(subset=['Year'])

    # Reset index after dropping rows
    df = df.reset_index(drop=True)

    return df

# Example usage
filename = 'ds140-gold-2022.xlsx'
data = get_commodity_data(filename)
data
