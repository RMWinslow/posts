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
from adjustText import adjust_text

# Data as (species, mercury, omega3) tuples
fish_data = [
    ("Striped Bass", 0.167, 0.8),
    ("Bluefish", 0.368, 1.2),
    ("Carp", 0.110, 0.6),
    ("Catfish", 0.024, 0.4),
    ("Clam", 0.009, 0.1),
    ("Cod", 0.111, 0.3),
    ("Crab", 0.065, 0.4),
    ("Atlantic Croaker", 0.069, 0.2),
    ("Flounder", 0.056, 0.2),
    ("Grouper", 0.448, 0.2),
    ("Haddock", 0.055, 0.2),
    # ("Halibut, Greenland", 0.241, 0.7),
    # ("Halibut, Pacific", 0.241, 0.5),
    ("Halibut", 0.241, 0.6),
    ("Atlantic Herring", 0.078, 1.7),
    ("Lobster", 0.093, 0.4),
    ("Atlantic Mackerel", 0.050, 2.6),
    ("Chub Mackerel", 0.088, 2.2),
    ("King Mackerel", 0.730, 2.2),
    ("Ocean Perch", 0.121, 0.2),
    ("Pollock", 0.031, 0.5),
    ("Sablefish", 0.361, 1.5),
    ("Atlantic Salmon", 0.078, 1.9),
    ("Sardines", 0.013, 1.4),
    ("Shrimp", 0.009, 0.5),
    ("Snapper", 0.166, 0.2),
    ("Swordfish", 0.995, 0.2),
    ("Freshwater Trout", 0.071, 2.0),
    ("Albacore Tuna", 0.354, 1.5),
    ("'Unspecified' Tuna", 0.398, 0.5),
    ("Whitefish", 0.089, 1.55),
    # from https://salmonfarmscience.wordpress.com/wp-content/uploads/2012/02/health_2008_omega3_in_fish_reduces_heart_disease.pdf
    # or https://pubmed.ncbi.nlm.nih.gov/18937898/
    # uses DHA+EPA; above numbers are DHA+EPA+LNA
    ("Shark", 0.979, 0.711/.85),
    ("Tilapia", 0.013, 0.115/.85),
    ("Orange Roughy", 0.571, 0.026/.85),
    ("Oysters", 0.012, .374/.85),
]


# Unzip the data for plotting
species, mercury, omega3 = zip(*fish_data)



# Determine a color for each species
# Several options I played around with are commented out.
# colors = [(hg/max(mercury),ω3/max(omega3),0.5) for sp, hg, ω3 in fish_data]
# colors = [(min(hg*3,1),ω3/max(omega3),0.6-hg/2) for sp, hg, ω3 in fish_data]
# def color_thresholds(hg,ω3):
#     if hg >= 0.3: return "red"
#     elif ω3 >= 1.0: return "green"
#     else: return "blue"
# colors = [color_thresholds(hg,ω3) for sp, hg, ω3 in fish_data]
colors = [(min(hg*4,1),ω3/max(omega3)*(1-hg),0.6-hg/2) for sp, hg, ω3 in fish_data]

plt.figure(figsize=(12, 8))
plt.scatter(mercury, omega3, c=colors, s=100, alpha=0.99, edgecolors="white")

# Add labels for each point
annotations = [plt.annotate(sp,(hg,ω3),xytext=(3,3),textcoords='offset points') for sp, hg, ω3 in fish_data]
# texts = [plt.text(hg, ω3, sp, ha='center', va='center') for sp, hg, ω3 in fish_data]
# adjust_text(texts, expand=(1.2, 2),)

plt.xlabel('Mercury (PPM)')
plt.ylabel('Omega-3 (g/100g of meat)')
plt.title('Mercury vs Omega-3 Levels in Seafood')
plt.grid(True, linestyle='--', alpha=0.7)


plt.text(
    0.6, 0.5, "blog.RMWinslow.com/fishchart", fontsize=40, color="grey", alpha=0.06,
    ha="center", va="center", rotation=-30, transform=plt.gca().transAxes
)



plt.tight_layout()
# plt.xscale("log")
# plt.yscale("log")

#set min values to zero
plt.xlim(0)
plt.ylim(0)

plt.savefig('babytips-fish.svg')
plt.savefig('babytips-fish.png')
plt.show()





#%%

'''
Other bookmarked links
https://www.npr.org/2006/10/17/6283905/fish-faq-what-you-need-to-know-about-mercury
WP cites the following for shark/tilefish ω3 content, but the source doesn't list the ω3 for those fish
https://www.ahajournals.org/doi/epub/10.1161/01.CIR.0000038493.65177.94

This fact sheet has the shark numbers but citation is unclear
https://nutrition.ucdavis.edu/sites/g/files/dgvnsk426/files/content/infosheets/factsheets/fact-pro-omega3.pdf

This page has similar-ish numbers and cites Harris et al. 2008
https://extension.colostate.edu/topic-areas/nutrition-food-safety-health/omega-3-fatty-acids-9-382/

Here's the Harris et al. paper (One of the authors is William S. Harris, who's affiliated with USD)
https://salmonfarmscience.wordpress.com/wp-content/uploads/2012/02/health_2008_omega3_in_fish_reduces_heart_disease.pdf

This page attributes that infographic that floats around to the Washington Post
https://www.allthingsgym.com/seafood-infographic-omega-3-vs-mercury-levels/
https://web.archive.org/web/20230620063546/https://www.washingtonpost.com/national/health-science/2012/04/03/gIQABd16sS_graphic.html
https://web.archive.org/web/20120410072053/https://www.washingtonpost.com/national/health-science/eat-more-fish-risks-overstated/2012/04/02/gIQARwPNrS_story.html
source is Joint FAO/WHO Expert Consultation on the Risks and Benefits of Fish Consumption
not sure which one
https://www.who.int/publications/i/item/9789241564311
https://www.who.int/publications/i/item/9789240100879


'''


# Comment detritus from the the LLM generation:
# Keeping this for the sake of notes/reference.
    # Salmon - This is just a placeholder note. The salmon data was all over the place.
    # For Mercury, I've averaged fresh/canned. For the Ω3, just used Atlantic.
    #("Herring", 0.078, {"Round": 1.3, "Atlantic": 1.7, "Pacific": 1.8, "Freshwater": 2.5}),
    #("Tuna (Fresh/Frozen, All)", 0.386, {"Albacore": 1.5, "Bluefin": 1.6}),
    #("Halibut", 0.241, {"Pacific": 0.5, "Greenland": 0.9}),
    #("Whitefish", 0.089, {"Lake Whitefish": 1.3, "Whitefish": 1.8}),
    #("Trout, Freshwater", 0.071, {"Siscowet": 4.6, "Lake": 2.0, "Lean Lake": 2.1, "Rainbow/Steelhead": 0.6}),
    #("Catfish", 0.024, {"Channel": 0.3, "Brown Bullhead": 0.5}),
    #("Crab", 0.065, {"Blue, canned": 0.4, "Alaskan King": 0.4}),