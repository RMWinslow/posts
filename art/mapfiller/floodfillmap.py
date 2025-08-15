#%% IMPORTS AND SETUP
from PIL import Image, ImageDraw
import numpy as np
from IPython.display import display # to display images in Jupyter Notebook

SOURCE_FILE = "blankusa.png" # Must be pure white with solid borders
img = Image.open(SOURCE_FILE, mode='r').convert("RGB")

blank_color = (255, 255, 255) # pure white
visited_color = (100,100,100)
active_color = (255, 0, 0)
size_threshold = 1000 # minimum size of a region to consider

image_regions = [] # regions are stored as numpy arrays of pixel coordinates
region_labels = []

#%% STEP 1: ITERATE THROUGH AND LABEL WHITE REGIONS, 
pixels = img.load()
for y in range(img.height):
    for x in range(img.width):
        if pixels[x, y] == blank_color:
            # highlight region & check size
            ImageDraw.floodfill(img, (x, y), active_color)
            region_pixels = np.where(np.array(img) == active_color)
            if len(region_pixels[0]) < size_threshold:
                ImageDraw.floodfill(img, (x, y), visited_color)
                continue
            image_regions.append(region_pixels)
            # user input
            display(img)
            user_input = input("Enter name of region: ")
            region_labels.append(user_input)
            # mark as visited
            ImageDraw.floodfill(img, (x, y), visited_color)
print(f"Found {len(image_regions)} white regions.")


# %%
