#%% https://fred.stlouisfed.org/release/tables?rid=53&eid=1228299

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as pe

# Data as list of (category, subcategory, color, value) tuples
budget_data = [
    ('Education', 'Elementary and secondary', '#FFD966', 1056.5),
    ('Education', 'Higher Ed', '#C0C0C0', 301.1),
    ('Education', 'other', '#FFB3D9', 46.5),
    
    ('National\nDefense', 'National defense', '#4A6FA5', 1082.7),
    
    ('Economic\naffairs', 'Highways', '#8C7A5F', 350.0),
    ('Economic\naffairs', 'Other\ntransp.', '#B3996B', 110.6),
    # ('Economic\naffairs', 'Other\ntransp.\nAir,Water,\nRail', '#B3996B', 110.6),
    # ('Economic\naffairs', 'SPACE!', "#FBEE5C", 41.9), 
    ('Economic\naffairs', 'SPACE!', "#000000", 41.9), 
    ('Economic\naffairs', 'Other\n(Ag., Energy, etc.)', '#A8C97A', 252.7),
    
    ('Public order\nand safety', 'Police', '#4D85CC', 254.2),
    ('Public order\nand safety', 'Prisons', '#94A8BA', 126.6),
    ('Public order\nand safety', 'Courts', "#F5F5DC", 83.9),
    ('Public order\nand safety', 'Fire', '#F28963', 85.5),
    
    ('General\npublic\nservice', 'Executive\nand\nlegislative', '#9D7DB8', 135.9),
    ('General\npublic\nservice', 'Tax\ncollection\nand\nfinancial\nmgmt.', '#BA9DD1', 121.4),
    ('General\npublic\nservice', 'Other', '#D6BDE8', 207.0),
    
    ('Health', 'Health', '#E85C5C', 448.6),
    
    ('Income\nsecurity', 'Income security', '#F5AD70', 175.7),
    
    ('Housing and\ncommunity\nservices', 'Housing and community services', '#C99D7F', 89.4),
    
    ('Recreation\nand culture', 'Recreation and culture', '#7AC9AD', 70.8),
]



# Extract unique categories while preserving order
categories = []
seen = set()
for category, _, _, _ in budget_data:
    if category not in seen:
        categories.append(category)
        seen.add(category)

# Group data by category for plotting
data_by_category = {cat: [] for cat in categories}
for category, subcategory, color, value in budget_data:
    data_by_category[category].append((subcategory, color, value))

# Plot setup
fig, ax = plt.subplots(figsize=(10, 10))
bar_height = 0.9
y = -np.arange(len(categories))  # Negative sign makes the first category appear at the top

# Create horizontal stacked bars with labels
for i, category in enumerate(categories):
    left = 0  # Track cumulative width for stacking
    subcomponents = data_by_category[category]
    for j, (subcomp, color, value) in enumerate(subcomponents):
        # Plot bar with specific color, higher zorder
        bar = ax.barh(y[i], value, bar_height, label=subcomp if i == 0 else None, 
                      left=left, color=color, zorder=2)
        # Add label on bar only if category has multiple subcomponents
        width = bar[0].get_width()
        if len(subcomponents) > 1 or width > 200: 
            # Rotate label 90 degrees if bar width is small (e.g., < 100)
            rotation = 90 if width < 80 else 0
            ax.text(left + width / 2, y[i], f'{subcomp}', 
                    ha='center', va='center', color='black', fontsize=9, rotation=rotation,
                    # path_effects=[pe.withStroke(linewidth=1.5, foreground="#fffd")],
                    # weight='bold' if rotation == 90 else 'normal',
            )
            if subcomp == 'SPACE!':
                ax.text(left + width / 2, y[i], f'{subcomp}', 
                        ha='center', va='center', color='white', fontsize=9, rotation=rotation,
                        weight='bold',
                )
        left += value

# Customize plot
ax.set_yticks(y)
ax.set_yticklabels(categories)
ax.set_xlabel('Billions of Dollars')
# ax.set_title('2024 US Government Consumption/Investment (Federal + State + Local) by Purpose - Table 3.15.5')
ax.set_title('2024 US Government Consumption & Investment, by Purpose', fontsize=16, weight='bold', pad=20)
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True, axis='x', linestyle='--', alpha=0.7, color='gray', zorder=1)  # Vertical gridlines behind bars

# Add info box in bottom right
info_text = '''Data Source: BEA NIPA Table 3.15.5
"Government Consumption Expenditures and Gross Investment by Function"
Includes Federal, State, and Local government.

Note: This doesn't include all government spending.
      Rather, this is government purchases of goods and services.
      These categories together make up the G part of C+I+G+NX.
      Overall Health spending is much higher, for example.

Plotted by: @RMWinslow'''

plt.text(0.35, 0.02, info_text, transform=ax.transAxes, fontsize=10, 
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'),
         ha='left')  # Left-align text within the box

plt.tight_layout()
plt.savefig('stacked_G_graph_2024.png', dpi=600, bbox_inches='tight')  # Export as PNG with 600 DPI
plt.show()
# %%
