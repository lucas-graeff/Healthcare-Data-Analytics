import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

#Create DataFrame from csv
dataFrame = pd.read_csv('data.csv')

#task 1: Clean up data table and creaete new table
newDataFrame = dataFrame[['Dim2ValueCode', 'FactValueNumeric']].copy()

#task 2: assign values to their designated age groups
years15_24_list = []
years25_34_list = []
years35_44_list = []
years45_54_list = []
years55_64_list = []
years65_74_list = []
years75_84_list = []
years85Plus_list = []

for index, row in newDataFrame.iterrows():
    #print(row["Dim2ValueCode"], row["FactValueNumeric"])
    
    if row["Dim2ValueCode"] == "YEARS15-24":
        years15_24_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS25-34":
        years25_34_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS35-44":
        years35_44_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS45-54":
        years45_54_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS55-64":
        years55_64_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS65-74":
        years65_74_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS75-84":
        years75_84_list.append(row["FactValueNumeric"])
    elif row["Dim2ValueCode"] == "YEARS85PLUS":
        years85Plus_list.append(row["FactValueNumeric"])
        
#task 3: get min values for each age group
years15_24_min = min(years15_24_list)
years25_34_min = min(years25_34_list)
years35_44_min = min(years35_44_list)
years45_54_min = min(years45_54_list)
years55_64_min = min(years55_64_list)
years65_74_min = min(years65_74_list)
years75_84_min = min(years75_84_list)
years85Plus_min = min(years85Plus_list)

print("Minimum values are...")
print("years 15-24: {}".format(years15_24_min))
print("years 25-34: {}".format(years25_34_min))
print("years 35-44: {}".format(years35_44_min))
print("years 45-54: {}".format(years45_54_min))
print("years 55-64: {}".format(years55_64_min))
print("years 65-74: {}".format(years65_74_min))
print("years 75-84: {}".format(years75_84_min))
print("years 85+: {}".format(years85Plus_min), end="\n\n")

        
#task 4: find 1st quartile values of data
years15_24_1stQuartile = np.quantile(years15_24_list, 0.25)
years25_34_1stQuartile = np.quantile(years25_34_list, 0.25)
years35_44_1stQuartile = np.quantile(years35_44_list, 0.25)
years45_54_1stQuartile = np.quantile(years45_54_list, 0.25)
years55_64_1stQuartile = np.quantile(years55_64_list, 0.25)
years65_74_1stQuartile = np.quantile(years65_74_list, 0.25)
years75_84_1stQuartile = np.quantile(years75_84_list, 0.25)
years85Plus_1stQuartile = np.quantile(years85Plus_list, 0.25)

print("1st Quartile values are...")
print("years 15-24: {}".format(years15_24_1stQuartile))
print("years 25-34: {}".format(years25_34_1stQuartile))
print("years 35-44: {}".format(years35_44_1stQuartile))
print("years 45-54: {}".format(years45_54_1stQuartile))
print("years 55-64: {}".format(years55_64_1stQuartile))
print("years 65-74: {}".format(years65_74_1stQuartile))
print("years 75-84: {}".format(years75_84_1stQuartile))
print("years 85+: {}".format(years85Plus_1stQuartile), end="\n\n")

#task 5: find median values of data
years15_24_median = statistics.median(years15_24_list)
years25_34_median = statistics.median(years25_34_list)
years35_44_median = statistics.median(years35_44_list)
years45_54_median = statistics.median(years45_54_list)
years55_64_median = statistics.median(years55_64_list)
years65_74_median = statistics.median(years65_74_list)
years75_84_median = statistics.median(years75_84_list)
years85Plus_median = statistics.median(years85Plus_list)

print("Median values are...")
print("years 15-24: {}".format(years15_24_median))
print("years 25-34: {}".format(years25_34_median))
print("years 35-44: {}".format(years35_44_median))
print("years 45-54: {}".format(years45_54_median))
print("years 55-64: {}".format(years55_64_median))
print("years 65-74: {}".format(years65_74_median))
print("years 75-84: {}".format(years75_84_median))
print("years 85+: {}".format(years85Plus_median), end="\n\n")

#task 6: find 3rd quartile values of data
years15_24_3rdQuartile = np.quantile(years15_24_list, 0.75)
years25_34_3rdQuartile = np.quantile(years25_34_list, 0.75)
years35_44_3rdQuartile = np.quantile(years35_44_list, 0.75)
years45_54_3rdQuartile = np.quantile(years45_54_list, 0.75)
years55_64_3rdQuartile = np.quantile(years55_64_list, 0.75)
years65_74_3rdQuartile = np.quantile(years65_74_list, 0.75)
years75_84_3rdQuartile = np.quantile(years75_84_list, 0.75)
years85Plus_3rdQuartile = np.quantile(years85Plus_list, 0.75)

print("3rd Quartile values are...")
print("years 15-24: {}".format(years15_24_3rdQuartile))
print("years 25-34: {}".format(years25_34_3rdQuartile))
print("years 35-44: {}".format(years35_44_3rdQuartile))
print("years 45-54: {}".format(years45_54_3rdQuartile))
print("years 55-64: {}".format(years55_64_3rdQuartile))
print("years 65-74: {}".format(years65_74_3rdQuartile))
print("years 75-84: {}".format(years75_84_3rdQuartile))
print("years 85+: {}".format(years85Plus_3rdQuartile), end="\n\n")

#task 7: find maximum values of data
years15_24_max = max(years15_24_list)
years25_34_max = max(years25_34_list)
years35_44_max = max(years35_44_list)
years45_54_max = max(years45_54_list)
years55_64_max = max(years55_64_list)
years65_74_max = max(years65_74_list)
years75_84_max = max(years75_84_list)
years85Plus_max = max(years85Plus_list)

print("Minimum values are...")
print("years 15-24: {}".format(years15_24_max))
print("years 25-34: {}".format(years25_34_max))
print("years 35-44: {}".format(years35_44_max))
print("years 45-54: {}".format(years45_54_max))
print("years 55-64: {}".format(years55_64_max))
print("years 65-74: {}".format(years65_74_max))
print("years 75-84: {}".format(years75_84_max))
print("years 85+: {}".format(years85Plus_max), end="\n\n")

#task 8: find interquartile ranges for each age group
years15_24_iqr = years15_24_3rdQuartile - years15_24_1stQuartile
years25_34_iqr = years25_34_3rdQuartile - years25_34_1stQuartile
years35_44_iqr = years35_44_3rdQuartile - years35_44_1stQuartile
years45_54_iqr = years45_54_3rdQuartile - years45_54_1stQuartile
years55_64_iqr = years55_64_3rdQuartile - years55_64_1stQuartile
years65_74_iqr = years65_74_3rdQuartile - years65_74_1stQuartile
years75_84_iqr = years75_84_3rdQuartile - years75_84_1stQuartile
years85Plus_iqr = years85Plus_3rdQuartile - years85Plus_1stQuartile

print("Interquartile Ranges are...")
print("years 15-24: {}".format(years15_24_iqr))
print("years 25-34: {}".format(years25_34_iqr))
print("years 35-44: {}".format(years35_44_iqr))
print("years 45-54: {}".format(years45_54_iqr))
print("years 55-64: {}".format(years55_64_iqr))
print("years 65-74: {}".format(years65_74_iqr))
print("years 75-84: {}".format(years75_84_iqr))
print("years 85+: {}".format(years85Plus_iqr), end="\n\n")

#task 9: find mean values of data
def find_mean(list):
    mean = sum(list)/len(list)
    return mean

years15_24_mean = find_mean(years15_24_list)
years25_34_mean = find_mean(years25_34_list)
years35_44_mean = find_mean(years35_44_list)
years45_54_mean = find_mean(years45_54_list)
years55_64_mean = find_mean(years55_64_list)
years65_74_mean = find_mean(years65_74_list)
years75_84_mean = find_mean(years75_84_list)
years85Plus_mean = find_mean(years85Plus_list)

print("Average values are...")
print("years 15-24: {}".format(years15_24_mean))
print("years 25-34: {}".format(years25_34_mean))
print("years 35-44: {}".format(years35_44_mean))
print("years 45-54: {}".format(years45_54_mean))
print("years 55-64: {}".format(years55_64_mean))
print("years 65-74: {}".format(years65_74_mean))
print("years 75-84: {}".format(years75_84_mean))
print("years 85+: {}".format(years85Plus_mean), end="\n\n")

#task 10: find standard deviation of data
years15_24_variance = statistics.pstdev(years15_24_list)
years25_34_variance = statistics.pstdev(years25_34_list)
years35_44_variance = statistics.pstdev(years35_44_list)
years45_54_variance = statistics.pstdev(years45_54_list)
years55_64_variance = statistics.pstdev(years55_64_list)
years65_74_variance = statistics.pstdev(years65_74_list)
years75_84_variance = statistics.pstdev(years75_84_list)
years85Plus_variance = statistics.pstdev(years85Plus_list)

print("Variance values are...")
print("years 15-24: {}".format(years15_24_variance))
print("years 25-34: {}".format(years25_34_variance))
print("years 35-44: {}".format(years35_44_variance))
print("years 45-54: {}".format(years45_54_variance))
print("years 55-64: {}".format(years55_64_variance))
print("years 65-74: {}".format(years65_74_variance))
print("years 75-84: {}".format(years75_84_variance))
print("years 85+: {}".format(years85Plus_variance), end="\n\n")

#task 11: create boxplots for suicide rates of each age group
box_plot_data = [years15_24_list, years25_34_list, years35_44_list, years45_54_list, years55_64_list, years65_74_list, years85Plus_list]

age_groups = ["15-24", "25-34", "35-44", "45-54", "55-64", "75-84", "85+"]

plt.xlabel("Age Groups")
plt.ylabel("Suicide Rates per 100,000 people")
plt.title("Suicide Rates per 100,000 Population")
plt.boxplot(box_plot_data, labels=age_groups)

plt.show()
