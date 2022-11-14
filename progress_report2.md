## General Description
For this prototype, I again decided to work in Python as I was having trouble with using Julia effectively. If possible, I would prefer to continue working in Python, as while I can understand the labs given in class well enough to reproduce them in Python, I have yet to become comfortable with writing in the Julia language. This may result in some extra work being required, but I believe that the tradeoff would be worthwhile for me.
I have largely completed the goal I set out in my original project plan, and I think I have a good idea of what I still need to do for the project. However, I have completed many but not all of the recommended goals for this checkpoint.
The prototype file can be found [here](https://github.com/dcc5480/ASTRO-497-Exoplanet-Project/blob/main/prototype2.py).

## Short Guide for Testing the Prototype
- Run prototype2.py
- Choose an existing filepath for saving downloaded datasets.
- Input a Kepler ID. (Kepler-10 should work well)
- Input a row value starting from 0. (0 works well with Kepler-10)
- Input a description from the available list. ("Lightcurve Long Cadence (CLC) - Q2" works well for this example)
- Close each graph to see the next one.
- The graphs displayed are the raw data, cleaned data, periodogram, and folded data in that order. In addition, the detected period is printed.

## Progress Outline
- Removed NaN and outliers from data.
- Flattened data using a Savitzky-Golay filter.
- Created box least squares periodogram models for the data.
- Found promising periods for multiple example planets.
- Begun working on data folding.
- Graphed raw data, cleaned data, periodograms, and folded data.
- Improved feedback and comments.

## Areas for Improvement
- Implement a more sophisticated model. One possibility would be a model for detecting multiple planets. 
- Integrate a method for determining the quality of results from the model.
- Flattening with the Savitzky-Golay filter seems unreliable for any one window size and polynomial degree.
- Data folding is highly unreliable thus far.
- Plotting models over the data, especially the folded data.
- Create a more user-friendly interface. This may be more difficult than I had initially planned.
