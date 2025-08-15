"""
Use floodfill to label to regions of a blank white map based on user input.
(skimage.measure.label is a ready-made function that can do something similar, iirc.)
2025-08-15
"""

#%% IMPORTS AND SETUP
from PIL import Image, ImageDraw
import numpy as np
import colorsys
from IPython.display import display # to display images in Jupyter Notebook

SOURCE_FILE = "foo2.png" # Must be pure white with solid borders
img = Image.open(SOURCE_FILE, mode='r').convert("RGB")

blank_color = (255, 255, 255) # pure white
visited_color = (100,100,100)
active_color = (255, 0, 0)

region_seeds = [] # starting points for pixel floodfills
region_labels = []

#%% STEP 1: ITERATE THROUGH AND LABEL WHITE REGIONS, 
pixels = img.load()
for y in range(img.height):
    for x in range(img.width):
        if pixels[x, y] == blank_color:
            # highlight region
            ImageDraw.floodfill(img, (x, y), active_color)
            region_seeds.append((x,y))
            # user input
            display(img)
            user_input = input("Enter name of region: ")
            region_labels.append(user_input)
            # mark as visited
            ImageDraw.floodfill(img, (x, y), visited_color)
print(f"Found {len(region_seeds)} white regions. Added {len(set(region_labels))} unique labels.")


#%% STEP 2: GENERATE A TERRIBLE COLOR PALETTE

def generate_random_palette(num_colors, seed=42):
    """generates 3 arrays of HSV values, shuffles, pairs, and converts to RGB"""
    N = num_colors + 4

    hues = np.linspace(0, 1, N, endpoint=False)
    saturations = np.linspace(0.5, 1.0, N)
    values = np.linspace(0.5, 1.0, N)

    np.random.seed(seed) 
    np.random.shuffle(hues)
    np.random.shuffle(saturations)
    np.random.shuffle(values)

    rgb_colors = [colorsys.hsv_to_rgb(h,s,v) for h,s,v in zip(hues,saturations,values)]
    rgb_colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in rgb_colors]
    return rgb_colors[:num_colors]

map_labelset = set(region_labels)
map_colorset = set(generate_random_palette(len(set(region_labels))))
assert len(map_labelset) == len(map_colorset), "lol, lmao try a different seed, ig"

label_to_color = dict(zip(map_labelset, map_colorset))
label_to_color[""] = blank_color


#%% STEP 3: FILL REGIONS WITH COLORS, OUTPUT RESULTS
for seed, label in zip(region_seeds, region_labels):
    color = label_to_color[label]
    ImageDraw.floodfill(img, seed, color)

display(img)

img.save(SOURCE_FILE.replace(".png", "_colored.png"))
with open(SOURCE_FILE.replace(".png", "_labels.txt"), "w") as f:
    for label, color in label_to_color.items():
        f.write(f"{label}: {color}\n")


# %%
