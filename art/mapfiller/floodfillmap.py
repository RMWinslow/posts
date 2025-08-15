#%%
import PIL
from PIL import Image, ImageDraw
import numpy as np
import random
from IPython.display import display

SOURCE_FILE = "blankusa.png"

img = Image.open(SOURCE_FILE, mode='r').convert("RGB")

#%% STEP 1: Count and mark the regions.
visited_color = (100,100,100)
active_color = (255, 0, 0)
image_regions = [] # list of sets of indices, each entry corresponds to a region

# Iterate through pixels. When we encounter a white pixel, 
# flood fill it with red, use red pixels to store a mask
# and increment the counter
pixels = img.load()
width, height = img.size
for y in range(height):
    for x in range(width):
        if pixels[x, y] == (255, 255, 255): # white
            count += 1
            ImageDraw.floodfill(img, (x, y), active_color)
            image_regions.append(np.where(np.array(img) == active_color))
            display(img)
            ImageDraw.floodfill(img, (x, y), visited_color)
print(f"Found {count} white regions.")

# display the image
display(img)

