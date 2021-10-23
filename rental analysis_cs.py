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

import numpy as np
import panel as pn  
from panel.interact import interact
from panel import widgets

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

file_city_path="C:/Users/CS_Knit_tinK_SC/Documents/GitHub/HW_5_PyViz_Inputs/Resources/sfo_neighborhoods_census_data.csv"

#file_path = Path("Resources/sfo_neighborhoods_census_data.csv")
sfo_data = pd.read_csv(file_city_path, index_col="year")
print(sfo_data.head())

#%%

# Housing Units Per Year

# In this section, you will calculate the number of housing units per year and 
# visualize the results as a bar chart using the Pandas plot function.

# Hint: Use the Pandas groupby function.

# Optional challenge: Use the min, max, and std to scale the y limits of the chart.

#%%

# Calculate the mean number of housing units per year (hint: use groupby) 
# mean_housing_units_year = sfo_data.groupby("year").mean()

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

avg_price_sqr_ft = mean_housing_units_year_all["sale_price_sqr_foot"]
avg_monthly_rent = mean_housing_units_year_all["gross_rent"]

avg_both = mean_housing_units_year_all[["sale_price_sqr_foot", "gross_rent"]]
print(avg_both.head())

#%%

# Create two line charts, one to plot the average sale price per square foot and another for average montly rent

# Line chart for average sale price per square foot

avg_price_sqr_ft.hvplot(title="Average_Price_per_SqFt_by_Year").opts(line_color='red')

#%%


# Line chart for average montly rent
avg_monthly_rent.hvplot(title="Average_Gross_Rent_by_Year").opts(line_color='blue')
#.opts(bgcolor='red') # oops, that's not what I'm looking for

#%%

# Average Prices by Neighborhood

# In this section, you will use hvplot to create two interactive visulizations 
# of average prices with a dropdown selector for the neighborhood. 
# The first visualization will be a line plot showing the trend of average 
# price per square foot over time for each neighborhood. 
# The second will be a line plot showing the trend of average montly rent over time for each neighborhood.

# Hint: It will be easier to create a new DataFrame from 
# grouping the data and calculating the mean prices for each year and neighborhood


#%%

# Group by year and neighborhood and then create a new dataframe of the mean values

# want to combine these two df.s
# avg_price_sqr_ft = mean_housing_units_year_all["sale_price_sqr_foot"]
# avg_monthly_rent = mean_housing_units_year_all["gross_rent"]

# note - answer has index iterated, different from year values

# avg_nbrhds_years = sfo_data.groupby("year", "neighborhood").average() -- nope

#avg_prices_nhbrhood = (
#    pd.concat([avg_price_sqr_ft, avg_monthly_rent], axis=1).dropna().reset_index()
#)

# Attempt #2
#avg_prices_nhbrhood_new = sfo_data.groupby(['neighborhood'])['sale_price_sqr_foot'].mean().reset_index()



# new_df = sfo_data.groupby(level=[0,1])

print(sfo_data.index.names)

sfo_data.reset_index(level=0, inplace=True)


#%%

new_df = sfo_data.set_index(['year', 'neighborhood'])


#%%

avg_prices_nhbrhood = new_df.groupby(level=[0,1])['sale_price_sqr_foot', 'gross_rent'].mean().reset_index()

#%%

df_costs_year_sorted=avg_prices_nhbrhood.sort_values(['year','sale_price_sqr_foot'], ascending=False)

#%%
#%%
#%%
avg_prices_nhbrhood.sort_index()

print(avg_prices_nhbrhood.head())

#%%

# Use hvplot to create an interactive line chart of the average price per sq ft.
# The plot should have a dropdown selector for the neighborhood
# Define function to choose a year

# Define function to choose a year
def choose_year(year):
    return year

#%%

# Declare one list of years to be used in a Panel select list
# list_of_years = ['2014', '2013', '2012', '2011', '2010']


#%%
# Declare one list of neighborhoods to be used in a Panel select list
list_of_neighborhoods = sfo_data['neighborhood'].tolist()
interact(choose_year, year=list_of_years)

avg_prices_nhbrhood.hvplot(y='year',
    x='sale_price_sqr_foot',
    title='Average Sale Price per Year (and chosen neighborhood)',
    groupby='neighborhood'
    )
#%%
# Use hvplot to create an interactive line chart of the average monthly rent.
# The plot should have a dropdown selector for the neighborhood
def choose_neighborhood(neighborhood):
    return neighborhood

# Declare one list of neighborhoods to be used in a Panel select list
list_of_neighborhoods = sfo_data['neighborhood'].tolist()

interact(choose_neighborhood, neighborhood=list_of_neighborhoods)

avg_prices_nhbrhood.hvplot(y='year',
        x='gross_rent', 
        title='Average Rent per Year (and chosen neighborhood)',
        groupby='neighborhood'
        )





#%%
#%%

# The Top 10 Most Expensive Neighborhoods

# In this section, you will need to calculate the 
# mean sale price per square foot for each neighborhood 
# and then sort the values to obtain the top 10 most expensive neighborhoods on average. 
# Plot the results as a bar chart.

#%%
#%%


# Calculate the mean sale-price-per-square-foot  for each neighborhood


mean_sale_price_sq_foot_all = sfo_data.groupby("neighborhood").mean()
#%%

mean_sale_price_sq_foot_all.reset_index(level=0, inplace=True)


#%%

#%%
# changed my mean_sale_price_sq_foot to starter program's df_costs

df_costs=mean_sale_price_sq_foot_all[["neighborhood", "sale_price_sqr_foot", "housing_units", "gross_rent"]]

#%%
df_costs_sorted=df_costs.sort_values(by='sale_price_sqr_foot', ascending=False) 
#%%


#%%

df_costs_sorted=df_costs_sorted.reset_index(drop=True)
#%%
print(df_costs_sorted.head(10))

#%%

df_expensive_neighborhoods=df_costs_sorted.head(10)

print(df_expensive_neighborhoods.head())
#%%

# Plotting the data from the top 10 expensive neighborhoods
df_expensive_neighborhoods.hvplot.bar(y='sale_price_sqr_foot',
                                      x='neighborhood', 
                                      title="Most Expensive Neighborhoods", 
                                      rot = 90
                                     )


#%%

# Comparing cost to purchase versus rental income

# In this section, you will use hvplot to create an 
# interactive visualization with a dropdown selector 
# for the neighborhood. 
# This visualization will feature a side-by-side comparison
#  of average price per square foot versus average montly rent by year.

# Hint: Use the hvplot parameter, groupby, to create a dropdown selector
#  for the neighborhood.


#%%

# Fetch the previously generated DataFrame that was grouped by year and neighborhood
print(avg_prices_nhbrhood.head())

#%%

# Plotting the data 
def choose_neighborhood(neighborhood):
    return neighborhood

# Declare one list of neighborhoods to be used in a Panel select list
list_of_neighborhoods = sfo_data['neighborhood'].tolist()

interact(choose_neighborhood, neighborhood=list_of_neighborhoods)

# avg_prices_nhbrhood.hvplot(y='year', x='sale_price_sqr_foot', groupby='neighborhood')
#sbs_neighborhood = avg_prices_nhbrhood.groupby(by="neighborhood").mean()

#avg_prices_nhbrhood.hvplot(y='year', x='gross_rent', groupby='neighborhood')

bar1 = avg_prices_nhbrhood.hvplot(
                y = ["sale_price_sqr_foot", "gross_rent"],
                x = "year",
                kind = "bar",
                groupby="neighborhood",
                title="Side-by-Side Comparison: Avg Price (SqFt) to Avg Mo Rent, by Year",
                rot=90
                )
bar1


#%%

# Neighborhood Map

# In this section, you will read in neighborhoods location data
#  and build an interactive map with the average house value per neighborhood. 
# Use a scatter_mapbox from Plotly express to create the visualization. 
# Remember, you will need your Mapbox API key for this.

#%%

# Load Location Data


file_coord_path="C:/Users/CS_Knit_tinK_SC/Documents/GitHub/HW_5_PyViz_Inputs/Resources/neighborhoods_coordinates.csv"


map_coord_data = pd.read_csv(file_coord_path)
print(map_coord_data.head())

#%%

# Data Preparation

# You will need to join the location data with the mean values per neighborhood.

#    Calculate the mean values for each neighborhood.

#    Join the average values with the neighborhood locations.


# Calculate the mean values for each neighborhood
print(df_costs.head())

#%%

# Join the average values with the neighborhood locations

# change column name to match map df

df_costs=df_costs.rename(columns={'neighborhood': 'Neighborhood'})

#%%

# join the two tables in to one

neighbor_all =pd.merge(df_costs, map_coord_data, on= 'Neighborhood')
print(neighbor_all)

#%%
#%%
#%%


# Mapbox Visualization

# Plot the average values per neighborhood using a Plotly express scatter_mapbox visualization.


#%%

# Set the mapbox access token
# Prep Token

# Read the Mapbox API key
load_dotenv()  # mac

# path = "C:/users/garth/.env"
home = Path.home() / ".env"  # windows 1/2
load_dotenv(home)  # windows 2/2

map_box_api = os.getenv("mapbox")

# Set the Mapbox API
px.set_mapbox_access_token(map_box_api)

# Create a scatter mapbox to analyze neighborhood info
# Plot Data
map_plot = px.scatter_mapbox(
    neighbor_all,  # replace with df to watch your computer slow to an absolute crawl!
    lat="Lat",
    lon="Lon",
    size="sale_price_sqr_foot",
    color="gross_rent",
    zoom=11
)

# Display the map
map_plot.show()


#%%
#%%
#%%

# Cost Analysis - Optional Challenge

# In this section, you will use Plotly express to create visualizations 
# that investors can use to interactively filter and explore 
# various factors related to the house value of the San Francisco's neighborhoods.

# Create a DataFrame showing the most expensive neighborhoods in San Francisco by year

#%%

# Fetch the data from all expensive neighborhoods per year.

#df_costs=df_costs.rename(columns={'neighborhood': 'Neighborhood'})

df_costs_year_sorted=df_costs_year_sorted.rename(columns={'neighborhood': 'Neighborhood'})
df_expensive_neighborhoods_per_year = df_costs_year_sorted[df_costs_year_sorted["Neighborhood"].isin(df_expensive_neighborhoods["neighborhood"])]
print(df_expensive_neighborhoods_per_year.head())


#%%

# df_costs_year_sorted=avg_prices_nhbrhood.sort_values(['year','sale_price_sqr_foot'], ascending=False)





