'''
mercury data: 
https://downloads.regulations.gov/FDA-2014-N-0595-0149/content.pdf
https://www.fda.gov/food/environmental-contaminants-food/mercury-levels-commercial-fish-and-shellfish-1990-2012

Ω3 data: 
https://seafood.oregonstate.edu/sites/agscid7/files/snic/omega-3-content-in-fish.pdf

I used Claude/ChatGPT to parse and combine the PDFs. 
~~The numbers here seem correct,~~ but Claude also missed some.
(The robots were less helpful for plotting the data.)

Actually, a lot of numbers were wrong in bizarre ways. I think I've fixed them now.
Oh well, this LLM-generated chart still saved a lot of time.
Useful as a starting point, but always double-check your data!
'''

#%%
import matplotlib.pyplot as plt

# Data as (species, mercury, omega3) tuples
fish_data = [
    ("Bass, Striped", 0.167, 0.8),
    ("Bluefish", 0.368, 1.2),
    ("Carp", 0.110, 0.6),
    ("Catfish", 0.024, 0.4),
    ("Clam", 0.009, 0.1),
    ("Cod", 0.111, 0.3),
    ("Crab", 0.065, 0.4),
    ("Croaker, Atlantic", 0.069, 0.2),
    ("Flounder", 0.056, 0.2),
    ("Grouper", 0.448, 0.2),
    ("Haddock", 0.055, 0.2),
    ("Halibut, Greenland", 0.241, 0.7),
    ("Halibut, Pacific", 0.241, 0.5),
    ("Herring, Atlantic", 0.078, 1.7),
    ("Lobster, Spiny", 0.093, 0.4),
    ("Mackerel, Atlantic", 0.050, 2.6),
    ("Mackerel, Chub", 0.088, 2.2),
    ("Mackerel, King", 0.730, 2.2),
    ("Perch, Ocean", 0.121, 0.2),
    ("Pollock", 0.031, 0.5),
    ("Sablefish", 0.361, 1.5),
    ("Salmon, Atlantic", 0.078, 1.7),
    ("Sardines", 0.013, 1.4),
    ("Shrimp", 0.009, 0.5),
    ("Snapper", 0.166, 0.2),
    ("Swordfish", 0.995, 0.2),
    ("Trout, Freshwater", 0.071, 2.0),
    ("Tuna, Albacore", 0.354, 1.5),
    ("Tuna, Unspecified", 0.398, 0.5),
    ("Whitefish", 0.089, 1.55),
]

# Comment detritus from the the LLM generation:
    # Salmon - This is just a placeholder note. The salmon data was all over the place.
    # For Mercury, I've averaged fresh/canned. For the Ω3, just used Atlantic.
    #("Herring", 0.078, {"Round": 1.3, "Atlantic": 1.7, "Pacific": 1.8, "Freshwater": 2.5}),
    #("Tuna (Fresh/Frozen, All)", 0.386, {"Albacore": 1.5, "Bluefin": 1.6}),
    #("Halibut", 0.241, {"Pacific": 0.5, "Greenland": 0.9}),
    #("Whitefish", 0.089, {"Lake Whitefish": 1.3, "Whitefish": 1.8}),
    #("Trout, Freshwater", 0.071, {"Siscowet": 4.6, "Lake": 2.0, "Lean Lake": 2.1, "Rainbow/Steelhead": 0.6}),
    #("Catfish", 0.024, {"Channel": 0.3, "Brown Bullhead": 0.5}),
    #("Crab", 0.065, {"Blue, canned": 0.4, "Alaskan King": 0.4}),

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
plt.savefig('babytips-fish.png')
plt.show()