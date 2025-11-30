# https://apps.bea.gov/scb/pdf/2008/03%20March/0308_primer.pdf
# https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/all-chapters.pdf#page=268
# https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/chapter-09.pdf

# TODO: Display amount under each bar segment if wide enough.

#%%

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as pe


def plot_budget_stacked_bars(budget_data, title, info_text, output_filename=None, 
                             figsize=(10,10), bar_height=0.9, dpi=600, xlim=None,
                             SHOW_VALUE=False,
                             border_width=1, border_color='black'):
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
                          left=left, color=color, zorder=2,
                          edgecolor=border_color, linewidth=border_width)
            # Add label on bar only if category has multiple subcomponents
            width = bar[0].get_width()
            if len(subcomponents) > 1 or width > 200: 
                # Rotate label 90 degrees if bar width is small (e.g., < 80)
                rotation = 90 if width < 80 else 0
                if rotation == 0 and SHOW_VALUE==True:
                    # append italicized value to label
                    subcomp = f'{subcomp}\n{value:.1f}'

                ax.text(left + width / 2, y[i], f'{subcomp}', 
                        ha='center', va='center', color='black', fontsize=9, rotation=rotation,
                        # linespacing=0.9
                        )
                
                # Special handling for 'SPACE!' label
                if subcomp == 'SPACE!':
                    ax.text(left + width / 2, y[i], f'{subcomp}', 
                            ha='center', va='center', color='white', fontsize=9, rotation=rotation,
                            weight='bold', 
                            # linespacing=0.9,
                            )
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

    # Set x-axis ticks and grid lines every 200 units
    ax.xaxis.set_major_locator(plt.MultipleLocator(200))
    ax.set_xticks(np.arange(0, ax.get_xlim()[1] + 200, 200))
    
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
    ('General\npublic\nservice', 'Financial\nmgmt.\nand tax\ncollection', '#BA9DD1', 121.4),
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
    figsize=(11,10),
    # xlim=(0,1500),
)

plt.show()
# %%




#%% Combined Gov Spending with Transfers and Interest Payments


# budget_data_2024_with_transfers_and_interest = budget_data_2024 + [
#     ('General\npublic\nservice', 'Interest payments', '#B0B0B0', 1397.6),
#     # Then the Current Transfers for each category
#     # ('General\npublic\nservice', 'Current transfers', '#D6BDE8', 74.2),
#     # ('National\nDefense', 'Current transfers', '#C0C0C0', 0.8),
#     # ('Public order\nand safety', 'Current transfers', "#F5F5DC", 0.5),
#     # ('Economic\naffairs', 'Current transfers', '#A8C97A', 11.5),
#     # ('Housing and\ncommunity\nservices', 'Current transfers', '#C99D7F', 1.2),
#     # ('Health', 'Current transfers', '#E85C5C', 2258.7),
#     # ('Recreation\nand culture', 'Current transfers', '#7AC9AD', 0.8),
#     # ('Education', 'Current transfers', '#FFB3D9', 132.3),
#     # ('Income\nsecurity', 'Current transfers', '#F5AD70', 2097.6),
#     # Subsidies and Current Transfers for each category
#     ('General\npublic\nservice', 'Subsidies & transfers', '#FF00FF', 74.2),
#     ('National\nDefense', 'Subsidies & transfers', '#FF00FF', 0.8),
#     ('Public order\nand safety', 'Subsidies & transfers', "#FF00FF", 0.5),
#     ('Economic\naffairs', 'Subsidies & transfers', '#FF00FF', 42.0),
#     ('Housing and\ncommunity\nservices', 'Subsidies & transfers', '#FF00FF', 64.0),
#     ('Health', 'Subsidies & transfers', '#FF00FF', 2259.7),
#     ('Recreation\nand culture', 'Subsidies & transfers', '#FF00FF', 0.8),
#     ('Education', 'Subsidies & transfers', '#FF00FF', 132.3),
#     ('Income\nsecurity', 'Subsidies & transfers', '#FF00FF', 2097.6),
# ]


TRANSFER_COLOR = '#f8f'  # bright magenta for transfers

budget_data_2024_with_transfers_and_interest = [
    ('Education', 'Elementary and secondary', '#FFD966', 1056.5),
    ('Education', 'Higher Ed', '#C0C0C0', 301.1),
    ('Education', 'other', '#FFB3D9', 46.5),
    ('Education', 'Transfers', TRANSFER_COLOR, 132.3), # sliver for transfers
    
    ('National\nDefense', 'National defense', '#4A6FA5', 1082.7),
    # 0.8 sliver for transfers (Really, then where does the military foreign aid go?)
    ('National\nDefense', '', TRANSFER_COLOR, 0.8), # sliver for transfers
    #TODO: Use Table 3.11.5 to break down into More detailed categories.


    ('Economic\naffairs', 'Highways', '#8C7A5F', 350.0),
    ('Economic\naffairs', 'Other\ntransp.', '#B3996B', 110.6),
    ('Economic\naffairs', 'SPACE!', "#000000", 41.9), 
    ('Economic\naffairs', 'Other\n(Ag., Energy, etc.)', '#A8C97A', 252.7),
    ('Economic\naffairs', 'Subsidies\n& Transfers', TRANSFER_COLOR, 56.3),

    
    ('Public order\nand safety', 'Police', '#4D85CC', 254.2),
    ('Public order\nand safety', 'Prisons', '#94A8BA', 126.6),
    ('Public order\nand safety', 'Courts', "#F5F5DC", 83.9),
    ('Public order\nand safety', 'Fire', '#F28963', 85.5),
    ('Public order\nand safety', '', TRANSFER_COLOR, 0.5), #sliver for transfers
    
    ('General\npublic\nservice', 'Executive\nand\nlegislative', '#9D7DB8', 135.9),
    ('General\npublic\nservice', 'Financial\nmgmt.\n and tax\ncollection', '#BA9DD1', 121.4),
    ('General\npublic\nservice', 'Other', '#D6BDE8', 207.0),
    ('General\npublic\nservice', 'Interest payments', '#8f9', 1397.6),
    ('General\npublic\nservice', 'Transfers', TRANSFER_COLOR, 117.3),


    	
    # Health	
    # Current Transfers (Medicare, Medicaid, etc.)	2258.7
    # Capital Transfers	11.4
    # Subsidies	1
    # Consumption Expenditures (net of fees)	306.5
    # Gross Investment	142
    # Per Table 3.12	
    # Medicaid	938.2
    # Medicare	1,102.40
    # Other Transfers	229.50
    # C+I for Health = 448.6

    # ('Health', 'Health', '#E85C5C', 448.6),
    # ('Health', 'Consumption\nexpenditures', '#E85C5C', 306.5),
    # ('Health', 'Current\ntransfers', '#F9A4A4', 2258.7),
    # ('Health', 'Subsidies', '#F5AD70', 1.0),
    # ('Health', 'Gross\nInvestment', '#7AC9AD', 142.0),
    # ('Health', 'Capital\ntransfers', '#E6B800', 11.4),

    # ('Health', 'Gov. Health Services\n(net of fees)', '#E85C5C', 306.5),
    # ('Health', 'Gross\nInvestment', '#E85C5C', 142.0),
    # ('Health', 'Government Health Consumption\nand Investment (net of fees)', '#E85C5C', 448.6), 
    ('Health', 'G', '#E85C5C', 448.6), 
    ('Health', 'Medicare', '#c33', 1102.4),
    ('Health', 'Medicaid', '#e68697', 938.2),
    ('Health', 'Other\nhealth\ntransfers', TRANSFER_COLOR, 229.5),
    ('Health', '', TRANSFER_COLOR, 1), #1 billion subsidy as sliver


    # C+Transfers / C+I
    # Income security	2265.4	Income security	175.7
    # Disability	368.4	    Disability	7.3
    # Retirement5	1328.7	    Retirement1	2.5
    # Welfare and social services	402.3	    Welfare and social services	147.2
    # Unemployment	36.7	    Unemployment	0
    # Other	129.4	    Other	18.6
    #
    # Current Transfers	2097.6
    # And Capital Transfers 15.2

    # ('Income\nsecurity', 'Welfare and \nsocial services', '#F5AD70', 402.3), #F9E2A4
    # ('Income\nsecurity', 'Disability', '#F9E2A4', 368.4), #F5AD70
    # ('Income\nsecurity', 'Retirement', '#F7C987', 1328.7),
    # ('Income\nsecurity', 'Unemp.', '#FADFAE', 36.7),
    # ('Income\nsecurity', 'Other', '#fea', 152.5),
    # # ('Income\nsecurity', 'Other', '#fea', 129.4),
    # # ('Income\nsecurity', 'Gross\nInvestment', '#F5AD70', 7.9),
    # # ('Income\nsecurity', 'Capital transfers', '#E6B800', 15.2),

    
    # # Todo: alternate breakdown based on Table 3.12
    # # per 3.12, Social Security is 1448, Veterans Pension and disability	180.5
    # # SNAP is 97.4
    # ('Income\nsecurity', 'Purchases', '#F5AD70', 175.7),
    # ('Income\nsecurity', 'Social Security', '#d98', 1448.0),
    # ('Income\nsecurity', 'Veterans\nPension\n& Disability', '#e6b', 180.5),
    # ('Income\nsecurity', 'SNAP', '#f9d', 97.4),
    # ('Income\nsecurity', 'SSI', '#fbb', 60),
    # ('Income\nsecurity', 'Unemp.', '#fcd', 36.7),
    # # ('Income\nsecurity', 'Other\ntransfers', '#fbc', 386.9), #2112.8-SS-VPD-SNAP
    # # ('Income\nsecurity', 'Other\ntransfers', TRANSFER_COLOR, 350.2), #2112.8-SS-VPD-SNAP-UI
    # ('Income\nsecurity', 'Other\ntransfers', TRANSFER_COLOR, 290.2), #2112.8-SS-VPD-SNAP-UI-SSI



    # And Here's another Where I try to get the DI and OASI from SSA
    # https://www.ssa.gov/oact/STATS/table4a4.html
    # Numbers don't quite add up right. 1448 vs (155+1316)=1471
    # Note: Most of the gap is from the 
    ('Income\nsecurity', 'G', '#F5AD70', 175.7),
    ('Income\nsecurity', 'Social Security Old Age and Survivors Benefits', '#E89FDD', 1316.0),
    ('Income\nsecurity', 'SS Disability\nInsurance', '#D770C8', 155),
    ('Income\nsecurity', 'SSI', '#ED7FD5', 60),
    ('Income\nsecurity', 'Veterans\nPension\n& Disability', '#FF99E6', 180.5),
    ('Income\nsecurity', 'Unemp. Ins.', '#FFB3E8', 36.7),
    ('Income\nsecurity', 'SNAP', '#fbb', 97.4),
    ('Income\nsecurity', 'Other\nincome security\ntransfers', TRANSFER_COLOR, 267.2), #2112.8-SS-VPD-SNAP-UI-SSI



    ('Housing and\ncommunity\nservices', 'G', '#C99D7F', 89.4), #Purchases
    ('Housing and\ncommunity\nservices', 'Subsidies\n& Transfers', TRANSFER_COLOR, 76.6),
    
    ('Recreation\nand culture', 'G', '#7AC9AD', 70.8),
    ('Recreation\nand culture', '', TRANSFER_COLOR, 0.8), # sliver for transfers


    # Not sure whether this should be its own line.
    # ('General\npublic\nservice', 'Net purchases of\nnon-produced\nassets', '#808080', 20.5),
    ('Net purchases of\nnon-produced\nassets', 'Net purchases of\nnon-produced\nassets', '#808080', 20.5),
]




info_text_2024 = '''Data Sources: BEA NIPA Tables 
    Table 3.15.5: "Government Consumption Expenditures and Gross Investment by Function"
    Table 3.16: "Government Current Expenditures by Function"
    Table 3.17: "Selected Government) Current and Capital Expenditures by Function"
    Table 3.12: "Government Social Benefits"

Totals include Federal, State, and Local government.

Note: Approximately 804 billion dollars of Government Consumption Expenditures
    are in the form of "Consumption of Fixed Capital" (depreciation). To get "Total government
    expenditures", eg for calculating net borrowing, you would add all of the above and then 
    subtract the Consumption of Fixed Capital.

Plotted by: @RMWinslow'''

# "Total Expenditure" would be the sum of all of the above, minus the Consumption of Fixed Capital.
# "Purchases" is shorthand for "Government Consumption Expenditures and Gross Investment".
# 

# Create the plot
fig, ax = plot_budget_stacked_bars(
    budget_data_2024_with_transfers_and_interest, 
    '2024 US Government Expenditures, by Purpose', 
    info_text_2024,
    output_filename='stacked_G_spending_graph_2024.png',
    figsize=(18,11),
    xlim=(0,2800),
    bar_height=0.9,
)

plt.show()
# %%
