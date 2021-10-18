# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:31:25 2021

@author: CS_Knit_tinK_SC
"""


# San Francisco Housing Cost Analysis

# In this assignment, you will perform fundamental analysis for the San Francisco housing market
#  to allow potential real estate investors to choose rental investment properties.

#%%

# imports
import panel as pn
pn.extension('plotly')
import plotly.express as px
import pandas as pd
import hvplot.pandas
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

#%%

# Read the Mapbox API key
load_dotenv()
map_box_api = os.getenv("mapbox")

#%%

# Load Data¶

# Read the census data into a Pandas DataFrame
#C:\Users\CS_Knit_tinK_SC\Documents\GitHub\HW_5_PyViz_Inputs\Resources\sfo_neighborhoods_census_data.csv

file_path="C:/Users/CS_Knit_tinK_SC/Documents/GitHub/HW_5_PyViz_Inputs/Resources/sfo_neighborhoods_census_data.csv"

#file_path = Path("Resources/sfo_neighborhoods_census_data.csv")
sfo_data = pd.read_csv(file_path, index_col="year")
print(sfo_data.head())

#%%

# Housing Units Per Year

# In this section, you will calculate the number of housing units per year and 
# visualize the results as a bar chart using the Pandas plot function.

# Hint: Use the Pandas groupby function.

# Optional challenge: Use the min, max, and std to scale the y limits of the chart.

#%%

# Calculate the mean number of housing units per year (hint: use groupby) 


mean_housing_units_year_all = sfo_data.groupby("year").mean()

#%%

mean_housing_units_year = mean_housing_units_year_all["housing_units"]

print(mean_housing_units_year.head())

#%%

# Save the dataframe as a csv file
mean_housing_units_year.to_csv("C:/Users/CS_Knit_tinK_SC/Documents/GitHub/HW_5_PyViz_Inputs/Resources/mean_hsg_unit_yr.csv", encoding='utf-8', index=False)

#%%

# Use the Pandas plot function to plot the average housing units per year.
# Note: You will need to manually adjust the y limit of the chart using the min and max values from above.

# Plot data using hvplot.bar
# mean_housing_units_year.hvplot.bar(x='year', y='housing_units', title="Housing Units in San Francisco from 2010 to 2016") 

# Optional Challenge: Use the min, max, and std to scale the y limits of the chart
max_value=max(mean_housing_units_year)
min_value=min(mean_housing_units_year)
print(f'Min value is {min_value}')
print(f'Max value is {max_value}')


#%%


mean_housing_units_year.hvplot.bar(x='year', y='housing_units').opts(yformatter="%.0f", ylim=(350000, 400000), title="Housing Units in San Francisco from 2010 to 2016") 
# putting min and max values in to axis isn't generating the best result just yet. 

#%%

# Average Housing Costs in San Francisco Per Year

# In this section, you will calculate the average monthly rent and 
# the average price per square foot for each year. 
# An investor may wish to better understand the sales price of the 
# rental property over time. For example, a customer will want to know 
# if they should expect an increase or decrease in the property 
# value over time so they can determine how long to hold the rental property. 
# Plot the results as two line charts.

# Optional challenge: Plot each line chart in a different color.

# avg_price_sqr_ft = mean_housing_units_year_all["sale_price_sqr_foot"]
# avg_monthly_rent = mean_housing_units_year_all["gross_rent"]

avg_both = mean_housing_units_year_all[["sale_price_sqr_foot", "gross_rent"]]

#%%