## General Description
For this prototype, I decided to work purely in Python on my local machine in order to make progress quickly, though I plan to use Julia to implement the final product. I aimed to accomplish the goals I set out in both the suggested and my proposed schedule, and I believe this prototype has done so adequately, but not perfectly.
The prototype file can be found [here](https://github.com/dcc5480/ASTRO-497-Exoplanet-Project/blob/main/prototype1.py).

## Progress Outline
- Successfully downloaded and plotted raw data.
- Created a prototype for easy selection of Kepler objects for analysis.
- Combines sequential data files in memory.
- Implememted a prototype system for reusing previously downloaded data.
- Provides warnings when data fails to download or is too small.
- Successfully tested on multiple data sets, including quarters from lightcurve short and long cadence for Kepler-2 and 3 b and c.
- Included an option to suppress "print" output, as this can be inconvenient, especially for large downloads.

## Areas for Improvement
- Download and reuse product lists to reduce download time.
- Create a more user-friendly interface for the dashboard.
- Identify problematic data.
- Include more options, such as PDCSAP vs SAP_FLUX.
- Test more cases.
- Automatically detect a default filepath
- Write more descriptive comments.
- Complete the rest of the goals for future checkpoints.
