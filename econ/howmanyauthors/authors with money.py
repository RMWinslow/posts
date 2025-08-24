#TODO: calculate gini coeff for income distribution of authors
# %%  TAKE 2, CHECK FOR INCOME AS WELL

import pandas as pd
import csv

df = pd.read_stata("usa_00014.dta")

#%% PROCESSING AND HELPERS
# codebook for industries
ind_code_to_desc = {}
with open('US2022C_INDP.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        ind_code_to_desc[int(row[0])] = row[1]
        ind_code_to_desc[row[0]] = row[1]

print("missing codes: ", set(df['us2022c_indp'].unique()) - set(ind_code_to_desc.keys()))

##%% apply codebook 
df['ind desc'] = df['us2022c_indp'].map(ind_code_to_desc)
df.head(20)

##%% Define format for results table
# It's a weighted crosstab, sorted by total counts
def crosstab(df, rowvar, colvar, weightvar='perwt'):
    crosstab = pd.crosstab(df[rowvar],df[colvar],values=df[weightvar],aggfunc='sum')
    crosstab['Total'] = crosstab.sum(axis=1)
    crosstab.loc['Total'] = crosstab.sum(axis=0)
    return crosstab.sort_values(by='Total', ascending=False, axis=0)



#%% FILTERING
# Restrict to "authors and writers" occupation code 2850
# df[df['occ'] == 2850]['occ1990'].value_counts() # (Interesting. Nine "military" occ1990 recodes.)
authors = df[df['occ'] == 2850]

# restrict to those with the "independent artists, writers, and performers" industry code 8564
# authors = authors[authors['us2022c_indp'] == '8564']

#restrict to those with personal income > 20k 
# (inctot is total personal income, incearn is personal income from earnings)
# I think incearn is better, since inctot incluedes 
authors = authors[authors['incearn'] >= 100000]
# authors = authors[authors['inctot'] > 20000]
# authors = authors[authors['inctot'] < 9999998] # remove unknowns and N/As. Should be redundant with incearn filter above
# authors = authors[authors['incwage'] >= 20000]

# authors = authors[authors['empstat']=='employed']


## %% RESULTS
crosstab(authors, 'ind desc', 'classwkr', 'perwt').drop('n/a',axis=1).head(11)
# I return 11 for top ten + total row



# %%

