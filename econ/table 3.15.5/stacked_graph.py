#%%

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as pe


def plot_budget_stacked_bars(budget_data, title, info_text, output_filename=None, 
                             figsize=(10,10), bar_height=0.9, dpi=600, xlim=None):
    """
    Create a horizontal stacked bar chart for budget data.
    
    Parameters:
    -----------
    budget_data : list of tuples
        List of (category, subcategory, color, value) tuples
        Example: [('Education', 'Elementary and secondary', '#FFD966', 1056.5), ...]
    title : str
        Title for the chart
    info_text : str
        Information text to display in bottom right info box
    output_filename : str, optional
        Filename to save the figure. If None, figure is not saved.
    figsize : tuple, optional
        Figure size (width, height). Default is (10, 10)
    bar_height : float, optional
        Height of each bar. Default is 0.9
    dpi : int, optional
        DPI for saved figure. Default is 600
    xlim : tuple, optional
        X-axis limits (min, max). If None, automatically determined.
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes objects
    """
    
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
    fig, ax = plt.subplots(figsize=figsize)
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
                # Rotate label 90 degrees if bar width is small (e.g., < 80)
                rotation = 90 if width < 80 else 0
                ax.text(left + width / 2, y[i], f'{subcomp}', 
                        ha='center', va='center', color='black', fontsize=9, rotation=rotation)
                
                # Special handling for 'SPACE!' label
                if subcomp == 'SPACE!':
                    ax.text(left + width / 2, y[i], f'{subcomp}', 
                            ha='center', va='center', color='white', fontsize=9, rotation=rotation,
                            weight='bold')
            left += value
    
    # Customize plot
    ax.set_yticks(y)
    ax.set_yticklabels(categories)
    ax.set_xlabel('Billions of Dollars')
    ax.set_title(title, fontsize=16, weight='bold', pad=20)
    ax.grid(True, axis='x', linestyle='--', alpha=0.7, color='gray', zorder=1)
    
    # Set x-axis limits if provided
    if xlim is not None:
        ax.set_xlim(xlim)
    
    # Add info box in bottom right
    plt.text(0.35, 0.02, info_text, transform=ax.transAxes, fontsize=10, 
             verticalalignment='bottom', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'),
             ha='left')
    
    plt.tight_layout()
    
    # Save figure if filename is provided
    if output_filename:
        plt.savefig(output_filename, dpi=dpi, bbox_inches='tight')
    
    return fig, ax



#%% TABLE 3.15.5 Government Consumption Expenditures and Gross Investment by Function
# Original budget data
budget_data_2024 = [
    ('Education', 'Elementary and secondary', '#FFD966', 1056.5),
    ('Education', 'Higher Ed', '#C0C0C0', 301.1),
    ('Education', 'other', '#FFB3D9', 46.5),
    
    ('National\nDefense', 'National defense', '#4A6FA5', 1082.7),
    
    ('Economic\naffairs', 'Highways', '#8C7A5F', 350.0),
    ('Economic\naffairs', 'Other\ntransp.', '#B3996B', 110.6),
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

title_2024 = '2024 US Government Consumption & Investment, by Purpose'

info_text_2024 = '''Data Source: BEA NIPA Table 3.15.5
"Government Consumption Expenditures and Gross Investment by Function"
Includes Federal, State, and Local government.

Note: This doesn't include all government spending.
    Rather, this is government purchases of goods and services.
    These categories together make up the G part of C+I+G+NX.
    Overall Health spending is much higher, for example.

Plotted by: @RMWinslow'''

# Create the plot
fig, ax = plot_budget_stacked_bars(
    budget_data_2024, 
    title_2024, 
    info_text_2024,
    output_filename='stacked_G_graph_2024.png',
)

plt.show()
# %%




#%% Combined Gov Spending with Transfers and Interest Payments

budget_data_2024_with_transfers_and_interest = budget_data_2024 + [
    ('General\npublic\nservice', 'Interest payments', '#B0B0B0', 1397.6),
    # Then the Current Transfers for each category
    # ('General\npublic\nservice', 'Current transfers', '#D6BDE8', 74.2),
    # ('National\nDefense', 'Current transfers', '#C0C0C0', 0.8),
    # ('Public order\nand safety', 'Current transfers', "#F5F5DC", 0.5),
    # ('Economic\naffairs', 'Current transfers', '#A8C97A', 11.5),
    # ('Housing and\ncommunity\nservices', 'Current transfers', '#C99D7F', 1.2),
    # ('Health', 'Current transfers', '#E85C5C', 2258.7),
    # ('Recreation\nand culture', 'Current transfers', '#7AC9AD', 0.8),
    # ('Education', 'Current transfers', '#FFB3D9', 132.3),
    # ('Income\nsecurity', 'Current transfers', '#F5AD70', 2097.6),
    # Subsidies and Current Transfers for each category
    ('General\npublic\nservice', 'Subsidies & transfers', '#FF00FF', 74.2),
    ('National\nDefense', 'Subsidies & transfers', '#FF00FF', 0.8),
    ('Public order\nand safety', 'Subsidies & transfers', "#FF00FF", 0.5),
    ('Economic\naffairs', 'Subsidies & transfers', '#FF00FF', 42.0),
    ('Housing and\ncommunity\nservices', 'Subsidies & transfers', '#FF00FF', 64.0),
    ('Health', 'Subsidies & transfers', '#FF00FF', 2259.7),
    ('Recreation\nand culture', 'Subsidies & transfers', '#FF00FF', 0.8),
    ('Education', 'Subsidies & transfers', '#FF00FF', 132.3),
    ('Income\nsecurity', 'Subsidies & transfers', '#FF00FF', 2097.6),
     
]

info_text_2024 = '''Data Sources: BEA NIPA Tables 3.15.5, 3.16, and 3.17
    Table 3.15.5: "Government Consumption Expenditures and Gross Investment by Function"
    Table 3.16: "Government Current Expenditures by Function"
    Table 3.17: "Selected Government Current and Capital Expenditures by Function"
This includes Federal, State, and Local government.

Note: A few spending line items are excluded. 
    To get "Total government expenditures", you'd need to add in Capital transfers, 
    Net purchases of non-produced assets, and subtract Consumption of fixed capital.
    
Plotted by: @RMWinslow'''

# Create the plot
fig, ax = plot_budget_stacked_bars(
    budget_data_2024_with_transfers_and_interest, 
    '2024 US Government Current Expenditures & Gross Investment, by Purpose', 
    info_text_2024,
    output_filename='stacked_G_spending_graph_2024.png',
    figsize=(16,10),
)

plt.show()
# %%
