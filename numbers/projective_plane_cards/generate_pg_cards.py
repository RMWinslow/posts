#
#%%

# plane data from here: https://ericmoorhouse.org/pub/planes/
PG4 = '''0 1 2 3 4
0 5 6 7 8
0 9 14 15 16
0 10 12 17 19
0 11 13 18 20
1 5 9 10 11
1 6 14 17 18
1 8 13 16 19
1 7 12 15 20
2 5 14 19 20
4 5 13 15 17
3 5 12 16 18
2 6 9 12 13
2 7 11 16 17
2 8 10 15 18
3 6 11 15 19
4 6 10 16 20
4 7 9 18 19
3 8 9 17 20
4 8 11 12 14
3 7 10 13 14'''

PG3 = '''0 1 2 3
0 4 5 6
0 8 9 12
0 7 10 11
1 4 7 8
1 6 9 11
1 5 10 12
3 4 9 10
2 4 11 12
2 5 7 9
3 6 7 12
3 5 8 11
2 6 8 10'''

data = [[int(n) for n in row.split()] for row in PG3.splitlines()]

categories = {
    "animals": ["frog","bird","fish","lion"],
    "sun": ["west","noon","east","night"],
    # "weather": ["clear","cloudy","snowy",]
    "hat": ["top hat","propeller cap","fez","beanie"],
    "season": ["fall","winter","spring","summer",],
}
num_to_component = dict()

## %% Map numbers to components
# start with horizon marker
# then each row with the horizon market represents a different category.

num_to_component[data[0][0]] = "horizon"
horizon_lines = [row for row in data if data[0][0] in row]
for line,category in zip(horizon_lines,categories):
    for num,cat_value in zip(set(line)-{data[0][0]}, categories[category]):
        num_to_component[num] = cat_value

for i,line in enumerate(data):
    # print(line)
    print(i,[num_to_component[num] for num in line])




# %%
