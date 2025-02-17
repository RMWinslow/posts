'''
mercury data: 
https://downloads.regulations.gov/FDA-2014-N-0595-0149/content.pdf
https://www.fda.gov/food/environmental-contaminants-food/mercury-levels-commercial-fish-and-shellfish-1990-2012

Ω3 data: 
https://seafood.oregonstate.edu/sites/agscid7/files/snic/omega-3-content-in-fish.pdf

I used Claude/ChatGPT to parse and combine the PDFs. The numbers here seem correct, but Claude also missed some.
(The robots were less helpful for plotting the data.)
'''

#%%
import matplotlib.pyplot as plt

# Data as (species, mercury, omega3) tuples
fish_data = [
    ("Mackerel, Atlantic", 0.050, 2.6),
    ("Mackerel, Chub", 0.088, 2.2),
    ("Mackerel, King", 0.730, 2.2),
    #("Salmon (Fresh/Frozen)", 0.022, {"Pink": 1.0, "Chinook": 1.5, "Atlantic farmed": 1.9}),
    #("Salmon (Canned)", 0.014, {"Pink": 1.0, "Chum": 1.3, "Sockeye": 1.4}),
    #("Herring", 0.078, {"Round": 1.1, "Atlantic": 1.7, "Pacific": 1.8, "Freshwater": 2.5}),
    ("Tuna, Albacore (Canned)", 0.350, 1.3),
    #("Tuna (Fresh/Frozen)", 0.386, {"Albacore": 1.5, "Bluefin": 1.6}),
    ("Bluefish", 0.368, 1.2),
    ("Pollock", 0.031, 0.5),
    #("Halibut", 0.241, {"Pacific": 0.5, "Greenland": 0.9}),
    ("Cod", 0.111, 0.3),
    ("Haddock", 0.055, 0.2),
    ("Croaker, Atlantic", 0.069, 0.2),
    ("Flounder", 0.056, 0.2),
    ("Grouper", 0.448, 0.2),
    ("Snapper", 0.166, 0.2),
    ("Swordfish", 0.995, 0.2),
    ("Sablefish", 0.361, 1.5),
    #("Whitefish", 0.089, {"Lake Whitefish": 1.3, "Whitefish": 1.8}),
    ("Carp", 0.110, 0.6),
    ("Perch, Ocean", 0.121, 0.2),
    ("Bass, Striped", 0.167, 0.8),
    #("Trout, Freshwater", 0.071, {"Lean Lake": 1.2, "Lake": 2.0, "Rainbow/Steelhead": 2.1}),
    #("Catfish", 0.024, {"Channel": 0.3, "Brown Bullhead": 0.4}),
    ("Shrimp", 0.009, 0.5),
    ("Clam", 0.009, 0.1),
    #("Crab", 0.065, {"Blue, canned": 0.4, "Alaskan King": 0.4}),
    ("Lobster, Spiny", 0.093, 0.4),
    ("Sardines (Canned)", 0.013, 1.4),
]



# Unzip the data for plotting
species, mercury, omega3 = zip(*fish_data)

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