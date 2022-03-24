import pandas as pd
import numpy as np

#Create DataFrame from csv
dataFrame = pd.read_csv('data.csv')

#task 1: Clean up data table and creaete new table
newDataFrame = dataFrame[['ParentLocationCode', 'ParentLocation', 'Location', 'Dim1', 'Dim2', 'Value']].copy()

#task 2: output new dataframe to CSV
#newDataFrame.to_csv('new.DataSourceA')

#task 3: create dataframe containing mean for suicide rates of men (ages 15-24)

#task 4: create dataframe containing mean for suicide rates of women (ages 15-24)

print(dataFrame)

print("Program finished successfully")