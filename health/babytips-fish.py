'''
mercury data: 
https://downloads.regulations.gov/FDA-2014-N-0595-0149/content.pdf
https://www.fda.gov/food/environmental-contaminants-food/mercury-levels-commercial-fish-and-shellfish-1990-2012

Ω3 data: 
https://seafood.oregonstate.edu/sites/agscid7/files/snic/omega-3-content-in-fish.pdf

I used Claude to parse and combine the PDFs. The numbers here seem correct, but Claude also missed some.
(Claude was less helpful for plotting the data.)
'''

#%%
import matplotlib.pyplot as plt

# Data as (species, mercury, omega3) tuples
fish_data = [
    ('Anchovy', 0.016, 1.4, 'European anchovy in omega-3 data'),
    ('Catfish', 0.024, 0.3, "Mercury data doesn't specify type; omega-3 data is for Channel catfish"),
    ('Clam', 0.009, 0.1, ''),
    ('Cod, Atlantic', 0.111, 0.3, ''),
    ('Crab', 0.065, 0.4, 'Mercury data includes Blue/King/Snow; omega-3 data specifies Blue/Alaskan King'),
    ('Flounder', 0.056, 0.2, 'Mercury data includes all flatfish (flounder/plaice/sole)'),
    ('Grouper', 0.448, 0.2, 'Omega-3 data specifically for Red grouper'),
    ('Haddock', 0.055, 0.2, ''),
    ('Halibut', 0.241, 0.5, 'Omega-3 data specifically for Pacific halibut'),
    ('Herring', 0.078, 1.7, 'Omega-3 data specifically for Atlantic herring'),
    ('Lobster', 0.093, 0.4, 'Using Spiny lobster data for both sources'),
    ('Mackerel (Atlantic)', 0.05, 2.6, ''),
    ('Mackerel (King)', 0.73, 2.2, ''),
    ('Mackerel (Chub)', 0.088, 2.2, ''),
    ('Mullet', 0.050, 0.6, 'Omega-3 data specifically for Striped mullet'),
    # ('Oyster', 0.012, 'Not listed', ''),
    ('Pollock', 0.031, 0.5, ''),
    ('Salmon (fresh)', 0.022, 1.9, 'Using Atlantic farmed salmon omega-3 value as representative'),
    ('Sardine', 0.013, 1.4, 'Omega-3 data is for canned sardines'),
    ('Shrimp', 0.009, 0.5, ''),
    ('Snapper', 0.166, 0.2, 'Omega-3 data specifically for Red snapper'),
    ('Swordfish', 0.995, 0.2, ''),
    ('Trout (freshwater)', 0.071, 0.6, 'Using Rainbow trout omega-3 value'),
    ('Tuna (unspecified)', 0.386, 0.5, 'Using "fresh/frozen, all" mercury value')
]



# Unzip the data for plotting
species, mercury, omega3, notes = zip(*fish_data)

plt.figure(figsize=(12, 8))
plt.scatter(mercury, omega3)

# Add labels for each point
for i, species_name in enumerate(species):
    plt.annotate(species_name, 
                (mercury[i], omega3[i]),
                xytext=(5, 5), 
                textcoords='offset points')

plt.xlabel('Mercury (PPM)')
plt.ylabel('Omega-3 (g/100g)')
plt.title('Mercury vs Omega-3 Levels in Seafood')
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
# plt.show()

plt.savefig('babytips-fish.svg')