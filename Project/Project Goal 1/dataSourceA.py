import pandas as pd
import numpy as np

#Create DataFrame from csv
dataFrame = pd.read_csv('data.csv')

#task 1: Clean up data table and creaete new table
newDataFrame = dataFrame[['ParentLocationCode', 'ParentLocation', 'Location', 'Dim1', 'Dim2', 'Value']].copy()

#task 2: output new dataframe to CSV
newDataFrame.to_csv('new.DataSourceA', index=False)
