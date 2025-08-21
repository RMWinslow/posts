#%%
import pandas as pd
import csv

df = pd.read_csv("2018-2022 employed authors and writers counts.csv")

# codebook for industries
ind_code_to_desc = {}
with open('US2022C_INDP.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        ind_code_to_desc[int(row[0])] = row[1]

# apply codebook 
df['ind desc'] = df['ind code'].map(ind_code_to_desc)
df.sort_values(by='employee', ascending=False, inplace=True)
df.head(20)

# See here for industry codes:
# https://usa.ipums.org/usa-action/variables/US2022C_1088#description_section
# codes converted to csv via llm
# (For some reason the csv provided by IPUMS has some missing codes.)

# %% 
