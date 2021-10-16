# Unit 6 - PyViz hw

Build a dashboard with charts, maps, and interactive visualizations that help customers explore the data and determine if they want to invest in rental properties.

Accomplish the following tasks:

1. [Complete a notebook of rental analysis](#Rental-Analysis).

2. [Create a dashboard of interactive visualizations to explore the market data](#Dashboard).

---

## Files

* [sfo_neighborhoods_census_data.csv](Starter_Code/Data/sfo_neighborhoods_census_data.csv)
* [neighborhoods_coordinates.csv](Starter_Code/Data/neighborhoods_coordinates.csv)
* [Rental Analysis Starter Jupyter Notebook](Starter_Code/rental_analysis.ipynb)
* [Dashboard Starter Jupyter Notebook](Starter_Code/dashboard.ipynb)

## Instructions

### Rental Analysis

Work out all of the calculations and visualizations in an analysis notebook. Then, copy it over to a dashboard and use Panel to create the final layout. In `rental_analysis.ipynb` do the following:

#### Housing Units Per Year

Calculate the number of housing units/year. Visualize the results as a bar chart using the Pandas plot function.

Optional: Use the min, max, and standard deviation of the data to manually scale the y limits of the plot.

Default Bar Chart

  ![unscaled-bar.png](Images/unscaled-bar.png)

Bar Chart with y-axis limits adjusted

  ![scaled-bar.png](Images/scaled-bar.png)


#### Average Housing Costs in San Francisco Per Year

Determine the average(sales price) per year and the average(gross rent) per year. E.g., should you expect an increase or decrease in the property value or rent over time? Visualize the average (mean) gross rent and average price per square foot per year and visualize it as a bar chart.

1. Calculate the annual mean `gross_rent` and `sale_price_sqr_foot`.
2. Visualize the annual mean `gross_rent` and `sale_price_sqr_foot` as two line charts.

  ![gross-rent.png](Images/gross-rent.png)

  ![average-sales.png](Images/average-sales.png)

#### Average Prices By Neighborhood

Use hvplot to create two interactive visulizations of average prices, with a neighborhood dropdown selection. 

Visualization 1 = line plot showing the trend of average price per square foot over time, per neighborhood.  

Visualization 2 = line plot showing the trend of average monthly rent over time, per neighborhood.

  ![avg-price-neighborhood.png](Images/avg-price-neighborhood.png)

  ![gross-rent-neighborhood.png](Images/gross-rent-neighborhood.png)


#### Top 10 Most Expensive Neighborhoods

Determine top 10 most expensive neighborhoods. Calculate the mean sale price per neighborhood, then sort to obtain the top 10 most expensive neighborhoods on average. Plot results as a bar chart.

  ![top-10-expensive-neighborhoods.png](Images/top-10-expensive-neighborhoods.png)


#### Comparing Cost to Purchase Versus Rental Income

Use `hvplot` to create an interactive visualization with a neighborhood dropdown selector. Make a side-by-side comparison of average price per square foot vs average monthly rent by year.

![rent-versus-price](Images/rent-versus-price.png)

#### Neighborhood Map

Read in neighborhood location data, build an interactive map with the average prices per neighborhood. Use plotly express scatter mapbox object. Use the API.

  ![neighborhood-map.png](Images/neighborhood-map.png)

####  **Optional**: Cost Analysis Challenge

Use plotly express to create a Parallel Coordinates plot, Parallel Categories plot, and a Sunburst plot, to enable user to interactively filter and explore various factors related to neighborhood sales price.

Use the provided DataFrame to:

Create a Parallel Coordinates Plot.

  ![parallel-coordinates.png](Images/parallel-coordinates.png)

2. Create a Parallel Categories Plot.

  ![parallel-categories.png](Images/parallel-categories.png)

3. Create a Sunburst plot to show the most expensive neighborhoods in San Francisco per year.

    ![sunburst](Images/sunburst.png)

---

### Dashboard

Use Panel to build an interactive dashboard for all visualizations. There are no hard requirements for the layout. Design it yourself.

Put dashboard code in dashboard.ipynb`. Copy the code for each visualization from the analysis notebook into separate functions (1 function per visualization). This will make it easier to build and modify the layout later. Each function should return the plot figure in a format that Panel can use to plot the visualization.

Sample Dashboard:

![dashboard-demo.gif](Images/dashboard-demo.gif)


### Submission

* Use the starter notebooks for the analysis and dashboard and upload these to Github.

* Complete your README to explain how to run and use your dashboard.

* Note: You should not submit your `mapbox` access token to Github!

* Submit the Github URL repository to Bootcampspot.
