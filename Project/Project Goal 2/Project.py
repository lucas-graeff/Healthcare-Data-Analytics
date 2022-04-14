import requests
import csv
import json
import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sea
import sklearn
from sklearn import svm, preprocessing

def getDescriptive(dataset, col):
    print(f'\n{col} Statistics')
    #Central Tendency
    mean = dataset[col].mean()
    median = dataset[col].median()
    mode = dataset[col].mode()
    #Spread
    range = round(dataset[col].max() - dataset[col].min(), 2)
    variance = dataset[col].var()
    std = dataset[col].std()

    print("Central Tendency")
    print("Mean:", round(mean, 2))
    print("Median:", median)
    print("Mode:", mode)
    print("\nSpread")
    print("Range:", range)
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(std, 2))
    # print("Interquartile Range:", iqr, "\n")


# x = requests.get('https://ghoapi.azureedge.net/api/MH_6')

# json_object = x.content.decode('utf-8')

# Writing to sample.json
# with open("Project Goal 2/sample.json", "w") as outfile:
#     outfile.write(json_object)

# json_file=open('Project Goal 2/sample.json','r')
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


#Data Preparation

#Convert to pandas datasets
suicide_df = pd.read_csv('suicide.csv', usecols = ['Location','Period', 'Dim1ValueCode', 'FactValueNumeric'])
psych_df = pd.read_csv('psych.csv', usecols = ['ParentLocation', 'Location', 'Period', 'Value'])

#Merge records
dataset = pd.merge(suicide_df, psych_df, how='left', left_on=['Location', 'Period'], right_on=['Location', 'Period'])
#Rename columns
dataset.rename(columns= {'ParentLocation':'Region', 'Location':'Country', 'FactValueNumeric':'SuicideRate', 'Value':'Psychiatrists'}, inplace = True)
# Drop rows that have nulls
dataset = dataset.dropna()
#Only use rows for both sexes
dataset.query("Dim1ValueCode == 'BTSX'", inplace=True)
#Drop sex and id column since they no longer needed
dataset.drop("Dim1ValueCode", axis=1, inplace=True)
# Sort alphabetically by country
dataset = dataset.sort_values('Country', ascending=True)
#Select subset of data by using 10-90 quartiles
quartile = dataset.quantile(q=[0.10, 0.90], numeric_only=True)
suicide_quartile = quartile.loc[:2, 'SuicideRate']
psych_quartile = quartile.loc[:2, 'Psychiatrists']
queryString = f'SuicideRate >= {suicide_quartile[0.10]} and SuicideRate <= {suicide_quartile[0.90]} and Psychiatrists >= {psych_quartile[0.10]} and Psychiatrists <= {psych_quartile[0.90]}'
dataset.query(queryString, inplace=True)
#Show correlation
print(dataset.corr())


#Descriptive Analytics
print(dataset['SuicideRate'].describe())
print(dataset['Psychiatrists'].describe())
# getDescriptive(dataset, 'SuicideRate')
# getDescriptive(dataset, 'Psychiatrists')

fig = px.scatter(dataset, x="SuicideRate", y="Psychiatrists", text="Country", color="Region", trendline="ols", trendline_scope="overall",  size_max=150)
fig.update_traces(textposition='top center')
fig.update_layout(
    height=1000,
    title_text='Suicide Rate and Psychatrists'
)
fig.show()

#Predictive Analytics

#Convert regions to numbers
dataset["Region"].astype("category").cat.codes
dataset = sklearn.utils.shuffle(dataset)

region_dict = {"Eastern Mediterranean": 1, "Europe": 2, "Western Pacific": 3, "South-East Asia": 4, "Americas": 5, "Africa": 6}
dataset['Region'] = dataset['Region'].map(region_dict)

x = dataset[['Psychiatrists', 'Region']]
x = preprocessing.scale(x)
y = dataset['SuicideRate']

test_size = 40

x_train = x[:-test_size]
y_train = y[:-test_size]

x_test = x[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel="linear")
clf.fit(x_train, y_train)

#Compare predictions with actual
print("\n Prediction results \n")
for x,y in zip(x_test, y_test):
    print(f"Model: {clf.predict([x])[0]}, Actual: {y}")
print(clf.score(x_test, y_test))

#Print dataset
print(dataset)
#Write to csv
dataset.to_csv('dataset.csv', index=False)