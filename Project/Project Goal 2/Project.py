import requests
import csv
import json
import numpy as np
import pandas as pd

x = requests.get('https://ghoapi.azureedge.net/api/MH_6')

json_object = x.content.decode('utf-8')

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

json_file=open('sample.json','r')
# csv_file=open('csv_format.csv','w')

# json_data_to_python_dict=json.load(json_file)
# write=csv.writer(csv_file)
# write.writerow(json_data_to_python_dict.keys())
# write.writerow(json_data_to_python_dict.values()[3])
# json_file.close()
# csv_file.close()

#Set 
# my_data = np.genfromtxt('suicide.csv', dtype=str, delimiter=',', usecols=np.arange(0,34))
# suicide_data = np.array(my_data)
# my_data = np.genfromtxt('psych.csv', dtype=str, delimiter=',', usecols=np.arange(0,34))
# psych_data = np.array(my_data)

#Convert to pandas datasets
suicide_df = pd.read_csv('suicide.csv', usecols = ['Location','Period', 'Dim1ValueCode', 'FactValueNumeric'])
psych_df = pd.read_csv('psych.csv', usecols = ['Location', 'Period', 'Value'])

print(suicide_df)
print(psych_df)
df3=pd.merge(suicide_df, psych_df, how='left', left_on=['Location', 'Period'], right_on=['Location', 'Period'])
# Drop rows that have nulls
df3 = df3.dropna()
df3 = df3.query("Dim1ValueCode == 'BTSX'")
# Sort alphabetically
print(df3.sort_values('Location', ascending=True))