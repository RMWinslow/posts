'''
Open 2024 data sources summary.xlsx
The source table and line columns indicate the location of the original data.
EG if source table is "3.16" and line is "2", then the data can be found in:
    a csv file called "./src/Table 3.16.csv"
    In a row whose first entry is "2"
    In a column which has the header 2024.
        But that's a bit tricky because there's some metadata at the top of the file.
        Assumption: The header row is the first to start with "Line" in the first column.

For each row with a non-empty source table and line,
    read the corresponding data from the BEA csv file,
    and update the value column summary.
Finally save the changes to the xlsx file without disturbing any other formatting. 
'''


#%%
import pandas as pd
import numpy as np
import openpyxl
import csv
import os
#%%
summary_path = "./2024 data sources summary.xlsx"
summary_df = pd.read_excel(summary_path, sheet_name=0, dtype=str)
#%%
def get_bea_value(table, line, year):
    bea_path = f"./src/Table {table}.csv"
    if not os.path.exists(bea_path):
        print(f"File not found: {bea_path}")
        return None
    with open(bea_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        # Find Column
        header_row = None
        for row in reader:
            if row and row[0].startswith("Line"):
                header_row = row
                break
        if header_row is None:
            print(f"No header row found in {bea_path}")
            return None
        year_index = None
        for i, col in enumerate(header_row):
            if col.strip() == str(year):
                year_index = i
                break
        if year_index is None:
            print(f"Year {year} not found in header of {bea_path}")
            return None
        f.seek(0)
        # find Line
        line = str(line).strip()
        for row in reader:
            if row and row[0].strip() == line:
                value_str = row[year_index].strip()
                try:
                    value = float(value_str.replace(',', ''))
                    return value
                except ValueError:
                    print(f"Invalid value '{value_str}' at Table {table}, Line {line}, Year {year}")
                    return None
        print(f"Line {line} not found in {bea_path}")
        return None

print(get_bea_value("3.16", "2", 2024))
#%%
year = 2024
for index, row in summary_df.iterrows():
    source_table = row['source table']
    source_line = row['line']
    summary_value = row['value']
    if pd.notna(source_table) and pd.notna(source_line):
        bea_value = get_bea_value(source_table, source_line, year)
        value_diff = bea_value - float(summary_value) if bea_value is not None and pd.notna(summary_value) else 'N/A'
        if value_diff != 0:
            print(f"{source_table},{source_line}: diff: {value_diff}")
# %%
# Now update the xlsx file with bea values and then make sure it's saved and closed properly.
year = 2024

# TODO



#close the workbook

# %%


