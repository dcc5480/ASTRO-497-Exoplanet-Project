## Purpose
The purpose of this dashboard will be to provide a convenient tool for analyzing transit light curves and using them to determine the periods and radii of exoplanets. Depending on time constraints, I would like to make the dashboard flexible, with options for different planets, data sources, and even different detection methods and data models.

## Data Acquisition
- Many projects collect exoplanet transit data, including the K2 phase of the Kepler space telescope and HATNet.
- K2 has data for over 3000 planet candidates, with hundreds of confirmed, unconfirmed, and false positive cases.
- Possible sources to download the data include the exoplanet archive and MAST.
- I plan to have some of the data downloaded and pre-processed for convenience, then have the option to import more data.
- The data will likely be in CSV format, though binary formats are also a good option.

## Data Wrangling
The data for each object may be in one or multiple tables, and the dashboard should automatically combine available data if necessary, removing unwanted columns and rows as well.

## Models
- A linear model to find MLEs for orbital parameters could be used as a baseline.
- A non-linear model with jitter using Turing could be a more robust model.
- The models will predict the transit depth, from which radius can be found, and period of the planet's orbit.
- The models can be assessed both by comparing predicted values to known values, and by comparing the results of different models to each other.

## Plots and Visualization
- Raw data, processed data without outliers, data with curve fits, and residuals with curve fits will all be shown in scatter plots
- There will mainly be scatter plots with curve fits, though other types of plots, such as periodograms, may prove useful as well.
- For lightcurves, the x-axis would be time in days, and the y-axis would be flux.
- Depending on the data, it is possible that points could be colored based on which observatories they are from.
- It is likely that including multiple panels could be useful to compare results between different models.
- These methods of visualization should encompass the most important information available on the dashboard, though it is quite possible that more methods will be added in the future as needed and for greater convenience.

## Schedule
- I plan to setup the template the dashboard and make progress on data downloading and wrangling by the first checkpoint so that it is easy to begin adding functions and plots and to begin experimenting with how to implement them. In the following weeks, I will begin to work on implementing the different models and some preliminary visualization and get a better idea of what will work best for the dashboard.
- For the second checkpoint, at least one of the models should be fully implemented and tested, and visualization should be in progress. At this point, I should be far enough along to know exactly how long it will take to finish the rest of the project.
- As I am not working with a team, that should not be an issue, and otherwise I am not presently aware of any hard scheduling constraints or preferences.
