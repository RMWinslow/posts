#%% copied from web chat prototype hashed out here: https://chatgpt.com/c/6a171e96-b238-8325-b5ea-acc9a7fc5c75


import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage.morphology import skeletonize

# Recreate the deterministic 32x32 height map.
n = 32
x = np.linspace(-1, 1, n)
y = np.linspace(-1, 1, n)
X, Y = np.meshgrid(x, y)

surface = (
    1.20 * np.exp(-((X + 0.25)**2 + (Y + 0.15)**2) / 0.20)
    + 0.75 * np.exp(-((X - 0.45)**2 + (Y - 0.35)**2) / 0.08)
    + 0.45 * np.exp(-((X + 0.55)**2 + (Y - 0.50)**2) / 0.12)
    - 0.35 * np.exp(-((X - 0.10)**2 + (Y + 0.55)**2) / 0.10)
)

surface_norm = (surface - surface.min()) / (surface.max() - surface.min())
height_map = np.rint(surface_norm * 10).astype(int)

# Skeletonize each connected terrace region using 8-connectivity.
skeleton_regions = []
all_skeleton = np.zeros_like(height_map, dtype=bool)

for level in range(11):
    mask = height_map == level

    # 3x3 structure means orthogonal + diagonal adjacency.
    labeled, num_components = ndimage.label(
        mask,
        structure=np.ones((3, 3), dtype=int)
    )

    for comp_id in range(1, num_components + 1):
        region = labeled == comp_id
        skel = skeletonize(region)

        skeleton_regions.append((level, comp_id, skel))
        all_skeleton |= skel

# Plot at higher DPI.
fig, ax = plt.subplots(figsize=(9, 9), dpi=220)

im = ax.imshow(
    height_map,
    origin="lower",
    interpolation="nearest",
    vmin=0,
    vmax=10
)

# Connect neighboring skeleton pixels within each skeleton with thin red lines.
# Only use "forward" directions to avoid drawing each edge twice.
neighbor_offsets = [
    (1, 0),    # right
    (0, 1),    # up
    (1, 1),    # up-right
    (1, -1),   # down-right
]

for level, comp_id, skel in skeleton_regions:
    ys, xs = np.nonzero(skel)

    for y0, x0 in zip(ys, xs):
        for dx, dy in neighbor_offsets:
            x1 = x0 + dx
            y1 = y0 + dy

            if (
                0 <= x1 < n
                and 0 <= y1 < n
                and skel[y1, x1]
            ):
                ax.plot(
                    [x0, x1],
                    [y0, y1],
                    color="red",
                    linewidth=0.6
                )

# Overlay skeleton pixels.
ys, xs = np.nonzero(all_skeleton)

ax.scatter(
    xs,
    ys,
    s=14,
    marker="o",
    facecolors="none",
    edgecolors="red",
    linewidths=0.9,
    label="skeleton pixels"
)

ax.set_title("32×32 Quantized Height Map with Connected Skeleton Overlay")
ax.set_xlabel("x index")
ax.set_ylabel("y index")

# Gridlines at cell boundaries.
ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
ax.grid(which="minor", linewidth=0.3)
ax.tick_params(which="minor", bottom=False, left=False)

# Major ticks every 4 cells.
ax.set_xticks(np.arange(0, n, 4))
ax.set_yticks(np.arange(0, n, 4))

ax.legend(loc="upper right")

cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("integer height value")

plt.show()

print(f"Rendered at DPI = {fig.dpi}")
print(f"Connected regions: {len(skeleton_regions)}")
print(f"Total skeleton pixels: {int(all_skeleton.sum())}")
# %%
