"""
Ethan Elfersy
N01360222
CAP4784 Intro to Data Analytics
"""

import pandas as pd
import numpy as np

raw_data = pd.read_csv("data.csv") # load csv data file into a dataframe

pd.set_option("display.max_columns", 15)    # make sure all columns of the data are displayed
pd.set_option("display.max_rows", 500)      # make sure enough rows are displayed
pd.set_option("display.max_colwidth", 500)  # make sure columns aren't truncated if the cells are very wide
pd.set_option("display.width", 1000)        # make the display wider so that it doesn't wrap

data = raw_data[['INDICATOR', 'UNIT', 'STUB_NAME', 'STUB_LABEL', 'YEAR', 'AGE', 'ESTIMATE']].copy()
data.dropna(inplace = True) # drop rows that are missing data
                            # (these are most likely demographics for which data had not been collected in a certain year)

# creating some data subsets; more can be made depending on the desired comparisons
male_data = data[(data["STUB_LABEL"] == "Male")]
female_data = data[(data["STUB_LABEL"] == "Female")]

#print("First 10 items:\n", raw_data.head(10))
#print("First 10 items:\n", data.head(10))
#print("First 10 items of data for males:\n", male_data.head(10))
#print("First 10 items of data for females:\n", female_data.head(10))