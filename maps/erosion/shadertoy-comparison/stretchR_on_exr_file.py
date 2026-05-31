#!/usr/bin/env python3
#%%
'''
This opens the red channel of an exr file,
And stretches a given range to file a 0-256 range.
'''

import OpenEXR
import Imath
import numpy as np
from PIL import Image


#%%
# ---- Parameters ----
MIN_VALUE = 0.0
MAX_VALUE = 1.0

def apply_stretcher(buffer_name):

    EXR_FILE = f"{buffer_name}.exr"
    OUTPUT_FILE = f"stretchedR-{buffer_name}.png"

    if MAX_VALUE <= MIN_VALUE:
        raise ValueError("MAX_VALUE must be greater than MIN_VALUE")

    exr = OpenEXR.InputFile(EXR_FILE)
    header = exr.header()

    dw = header["dataWindow"]
    width = dw.max.x - dw.min.x + 1
    height = dw.max.y - dw.min.y + 1

    channels = header["channels"].keys()

    if "R" in channels:
        channel_name = "R"
    elif "X" in channels:
        channel_name = "X"
    else:
        raise ValueError("EXR must contain an 'R' or 'X' channel")

    pixel_type = Imath.PixelType(Imath.PixelType.FLOAT)
    raw = exr.channel(channel_name, pixel_type)

    data = np.frombuffer(raw, dtype=np.float32).reshape(height, width)

    # Clamp, normalize to 0–1, then scale to 0–255
    data = np.clip(data, MIN_VALUE, MAX_VALUE)
    data = (data - MIN_VALUE) / (MAX_VALUE - MIN_VALUE)
    data = (data * 255.0).round().astype(np.uint8)

    Image.fromarray(data, mode="L").save(OUTPUT_FILE)

for testnum in '1234':
    for buffertype in 'ab':
        buffer_name = f"test{testnum}-buffer-{buffertype}"
        apply_stretcher(buffer_name)


# %%
