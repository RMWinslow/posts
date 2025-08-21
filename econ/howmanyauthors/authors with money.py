# %%  TAKE 2, CHECK FOR INCOME AS WELL

import pandas as pd
import csv

df = pd.read_stata("usa_00014.dta")

#%% CODEBOOK FOR INDUSTRIES

# codebook for industries
ind_code_to_desc = {}
with open('US2022C_INDP.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        ind_code_to_desc[int(row[0])] = row[1]

# apply codebook 
df['ind desc'] = df['us2022c_indp'].map(ind_code_to_desc)
df.head(20)



# %%

df