"""
Ethan Elfersy
N01360222
CAP4784 Intro to Data Analytics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = pd.read_csv("data.csv") # load csv data file into a dataframe

pd.set_option("display.max_columns", 15)    # make sure all columns of the data are displayed
pd.set_option("display.max_rows", 500)      # make sure enough rows are displayed
pd.set_option("display.max_colwidth", 500)  # make sure columns aren't truncated if the cells are very wide
pd.set_option("display.width", 1000)        # make the display wider so that it doesn't wrap

data = raw_data[['INDICATOR', 'UNIT', 'STUB_NAME', 'STUB_LABEL', 'YEAR', 'AGE', 'ESTIMATE']].copy()
data.dropna(inplace = True) # drop rows that are missing data
                            # (these are most likely demographics for which data had not been collected in a given year)

# creating some data subsets; more can be made depending on the desired comparisons
all_persons_data = data[(data["STUB_LABEL"] == "All persons") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
male_data = data[(data["STUB_LABEL"] == "Male") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
female_data = data[(data["STUB_LABEL"] == "Female") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

wh_male_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Male: White") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
bl_male_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Male: Black or African American") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
na_male_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Male: American Indian or Alaska Native") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
ap_male_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Male: Asian or Pacific Islander") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

wh_female_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Female: White") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
bl_female_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Female: Black or African American") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
na_female_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Female: American Indian or Alaska Native") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
ap_female_data = data[(data["STUB_NAME"] == "Sex and race") & (data["STUB_LABEL"] == "Female: Asian or Pacific Islander") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

hi_male_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Male: Hispanic or Latino: All races") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
hi_female_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Female: Hispanic or Latino: All races") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

wh_nh_male_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Male: Not Hispanic or Latino: White") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
bl_nh_male_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Male: Not Hispanic or Latino: Black or African American") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
na_nh_male_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Male: Not Hispanic or Latino: American Indian or Alaska Native") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
ap_nh_male_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Male: Not Hispanic or Latino: Asian or Pacific Islander") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

wh_nh_female_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Female: Not Hispanic or Latino: White") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
bl_nh_female_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Female: Not Hispanic or Latino: Black or African American") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
na_nh_female_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Female: Not Hispanic or Latino: American Indian or Alaska Native") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]
ap_nh_female_data = data[(data["STUB_NAME"] == "Sex and race and Hispanic origin") & (data["STUB_LABEL"] == "Female: Not Hispanic or Latino: Asian or Pacific Islander") & (data["UNIT"] == "Deaths per 100,000 resident population, age-adjusted")]

sr_data = data[(data["STUB_NAME"] == "Sex and race (Single race)")]

# finding mean values to include in a data visualization, rounded to 2 decimals
mean_males = round(male_data.ESTIMATE.mean(), 2)
mean_females = round(female_data.ESTIMATE.mean(), 2)

mean_wh_males = round(wh_male_data.ESTIMATE.mean(), 2)
mean_bl_males = round(bl_male_data.ESTIMATE.mean(), 2)
mean_na_males = round(na_male_data.ESTIMATE.mean(), 2)
mean_ap_males = round(ap_male_data.ESTIMATE.mean(), 2)

mean_wh_females = round(wh_female_data.ESTIMATE.mean(), 2)
mean_bl_females = round(bl_female_data.ESTIMATE.mean(), 2)
mean_na_females = round(na_female_data.ESTIMATE.mean(), 2)
mean_ap_females = round(ap_female_data.ESTIMATE.mean(), 2)

mean_hi_males = round(hi_male_data.ESTIMATE.mean(), 2)
mean_hi_females = round(hi_female_data.ESTIMATE.mean(), 2)

mean_wh_nh_males = round(wh_nh_male_data.ESTIMATE.mean(), 2)
mean_bl_nh_males = round(bl_nh_male_data.ESTIMATE.mean(), 2)
mean_na_nh_males = round(na_nh_male_data.ESTIMATE.mean(), 2)
mean_ap_nh_males = round(ap_nh_male_data.ESTIMATE.mean(), 2)

mean_wh_nh_females = round(wh_nh_female_data.ESTIMATE.mean(), 2)
mean_bl_nh_females = round(bl_nh_female_data.ESTIMATE.mean(), 2)
mean_na_nh_females = round(na_nh_female_data.ESTIMATE.mean(), 2)
mean_ap_nh_females = round(ap_nh_female_data.ESTIMATE.mean(), 2)

# building dataframes with mean data from subsets and creating bar plots from them

# the 1st bar plot is built from male and female data including Hispanics and Latinos
mean_male_data = [mean_wh_males, mean_bl_males, mean_na_males, mean_ap_males, mean_hi_males]
mean_female_data = [mean_wh_females, mean_bl_females, mean_na_females, mean_ap_females, mean_hi_females]
index = ["White", "Black/African-American", "Native American/Alaskan", "Asian/Pacific Islander", "Hispanic/Latino, All Races"]
mean_data = pd.DataFrame({"Male": mean_male_data, "Female": mean_female_data}, index = index)
mean_plot = mean_data.plot.bar(rot = 0), \
            plt.title("Mean age-adjusted US suicide by race and Hispanic origin"), \
            plt.xlabel("Race"), \
            plt.ylabel("Deaths per 100,000 people")

# the 2nd bar plot is built from male and female data excluding Hispanics and Latinos
mean_nh_male_data = [mean_wh_nh_males, mean_bl_nh_males, mean_na_nh_males, mean_ap_nh_males]
mean_nh_female_data = [mean_wh_nh_females, mean_bl_nh_females, mean_na_nh_females, mean_ap_nh_females]
nh_index = ["White", "Black/African-American", "Native American/Alaskan", "Asian/Pacific Islander"]
mean_nh_data = pd.DataFrame({"Male": mean_nh_male_data, "Female": mean_nh_female_data}, index = nh_index)
mean_nh_plot = mean_nh_data.plot.bar(rot = 0), \
               plt.title("Mean age-adjusted US suicide by race"), \
               plt.xlabel("Race"), \
               plt.ylabel("Deaths per 100,000 people")

# creating dataframes including certain year ranges and making line plots from them
male_data_from_1999 = male_data.iloc[22:]     # start at index 22 to exclude years through 1998
female_data_from_1999 = female_data.iloc[22:] # ditto

wh_nh_male_data_from_1999 = wh_nh_male_data[14:] # start at index 14 because earliest data is from 1985
bl_nh_male_data_from_1999 = bl_nh_male_data      # earliest data is from 1999
na_nh_male_data_from_1999 = na_nh_male_data      # ditto
ap_nh_male_data_from_1999 = ap_nh_male_data      # ditto
hi_male_data_from_1999 = hi_male_data[14:]       # start at index 14 because earliest data is from 1985

wh_nh_female_data_from_1999 = wh_nh_female_data[14:] # start at index 14 because earliest data is from 1985
bl_nh_female_data_from_1999 = bl_nh_female_data      # earliest data is from 1999
na_nh_female_data_from_1999 = na_nh_female_data      # ditto
ap_nh_female_data_from_1999 = ap_nh_female_data      # ditto
hi_female_data_from_1999 = hi_female_data[14:]       # start at index 14 because earliest data is from 1985

# 1st line plot shows non-Hispanic male data alongside data for Hispanic males
x = male_data_from_1999.YEAR
y1 = male_data_from_1999.ESTIMATE
y2 = wh_nh_male_data_from_1999.ESTIMATE
y3 = bl_nh_male_data_from_1999.ESTIMATE
y4 = na_nh_male_data_from_1999.ESTIMATE
y5 = ap_nh_male_data_from_1999.ESTIMATE
y6 = hi_male_data_from_1999.ESTIMATE
male_line_plot = plt.figure(), \
                 plt.plot(x, y1, label = "Total"), \
                 plt.plot(x, y2, label = "White"), \
                 plt.plot(x, y3, label = "Black/African-American"), \
                 plt.plot(x, y4, label = "Native American/Alaskan"), \
                 plt.plot(x, y5, label = "Asian/Pacific Islander"), \
                 plt.plot(x, y6, label = "Hispanic/Latino (All races)"), \
                 plt.legend(), \
                 plt.title("Age-adjusted US male suicide rate by race, 1999-2018"), \
                 plt.ylabel("Deaths per 100,000 people"), plt.xticks(np.arange(min(x), max(x) + 1, 1.0))

# 2nd line plot shows non-Hispanic female data alongside data for Hispanic females
x = male_data_from_1999.YEAR
y1 = female_data_from_1999.ESTIMATE
y2 = wh_nh_female_data_from_1999.ESTIMATE
y3 = bl_nh_female_data_from_1999.ESTIMATE
y4 = na_nh_female_data_from_1999.ESTIMATE
y5 = ap_nh_female_data_from_1999.ESTIMATE
y6 = hi_female_data_from_1999.ESTIMATE
female_line_plot = plt.figure(), \
                   plt.plot(x, y1, label="Total"), \
                   plt.plot(x, y2, label="White"), \
                   plt.plot(x, y3, label="Black/African-American"), \
                   plt.plot(x, y4, label="Native American/Alaskan"), \
                   plt.plot(x, y5, label="Asian/Pacific Islander"), \
                   plt.plot(x, y6, label="Hispanic/Latino (All races)"), \
                   plt.legend(), \
                   plt.title("Age-adjusted US female suicide rate by race, 1999-2018"), \
                   plt.ylabel("Deaths per 100,000 people"), plt.xticks(np.arange(min(x), max(x) + 1, 1.0))

# calculate mean % change from 1999-2018
print("Mean yearly % change from 1999 to 2018 for all males:", round((male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic White males:", round((wh_nh_male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Black males:", round((bl_nh_male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Native American males:", round((na_nh_male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Asian males:", round((ap_nh_male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for Hispanic males:", round((hi_male_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))

print("Mean yearly % change from 1999 to 2018 for all females:", round((female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic White females:", round((wh_nh_female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Black females:", round((bl_nh_female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Native American females:", round((na_nh_female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for non-Hispanic Asian females:", round((ap_nh_female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))
print("Mean yearly % change from 1999 to 2018 for Hispanic females:", round((hi_female_data_from_1999["ESTIMATE"].pct_change() * 100).mean(), 2))

# calculate total % change from 1999-2018
print("Total % change from 1999 to 2018 for all males:", round((male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic White males:", round((wh_nh_male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic Black males:", round((bl_nh_male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic Native American males:", round((na_nh_male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total yearly % change from 1999 to 2018 for non-Hispanic Asian males:", round((ap_nh_male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total yearly % change from 1999 to 2018 for Hispanic males:", round((hi_male_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))

print("Total % change from 1999 to 2018 for all females:", round((female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic White females:", round((wh_nh_female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic Black females:", round((bl_nh_female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total % change from 1999 to 2018 for non-Hispanic Native American females:", round((na_nh_female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total yearly % change from 1999 to 2018 for non-Hispanic Asian females:", round((ap_nh_female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))
print("Total yearly % change from 1999 to 2018 for Hispanic females:", round((hi_female_data_from_1999["ESTIMATE"].pct_change(periods = 19) * 100).mean(), 2))

# NOTE - to view results from the statements below, uncomment the desired lines
#      - to comment/uncomment multiple lines at once, select them and use the shortcut Ctrl+/ (PyCharm)

#print("First 10 items:\n", raw_data.head(10))
#print("First 10 items:\n", data.head(10))

"""MALES"""
# print("Data for males:\n", male_data)
# print("Descriptive statistics for males:\n", male_data.ESTIMATE.describe().round(2))

"""FEMALES"""
#print("Data for females:\n", female_data)
#print("Descriptive statistics for females:\n", female_data.ESTIMATE.describe().round(2))

"""MALES, WHITE"""
# print("Data for White males:\n", wh_male_data)
# print("Descriptive statistics for White males:\n", wh_male_data.ESTIMATE.describe().round(2))

"""MALES, BLACK/AFRICAN-AMERICAN"""
#print("Data for Black/African-American males:\n", bl_male_data)
#print("Descriptive statistics for Black/African-American males:\n", bl_male_data.ESTIMATE.describe().round(2))

"""MALES, NATIVE AMERICAN/ALASKAN"""
#print("Data for Native American/Alaskan males:\n", na_male_data)
#print("Descriptive statistics for Native American/Alaskan males:\n", na_male_data.ESTIMATE.describe().round(2))

"""MALES, ASIAN/PACIFIC ISLANDER"""
#print("Data for Asian/Pacific Islander males:\n", ap_male_data)
#print("Descriptive statistics for Asian/Pacific Islander males:\n", ap_male_data.ESTIMATE.describe().round(2))

"""MALES, HISPANIC/LATINO"""
# print("Data for all Hispanic/Latino males:\n", hi_male_data)
# print("Descriptive statistics for all Hispanic/Latino males:\n", hi_male_data.ESTIMATE.describe().round(2))

"""FEMALES, WHITE"""
#print("Data for White females:\n", wh_female_data)
#print("Descriptive statistics for White females:\n", wh_female_data.ESTIMATE.describe().round(2))

"""FEMALES, BLACK/AFRICAN-AMERICAN"""
#print("Data for Black/African-American females:\n", bl_female_data)
#print("Descriptive statistics for Black/African-American females:\n", bl_female_data.ESTIMATE.describe().round(2))

"""FEMALES, NATIVE AMERICAN/ALASKAN"""
#print("Data for Native American/Alaskan females:\n", na_female_data)
#print("Descriptive statistics for Native American/Alaskan females:\n", na_female_data.ESTIMATE.describe().round(2))

"""FEMALES, ASIAN/PACIFIC ISLANDER"""
#print("Data for Asian/Pacific Islander females:\n", ap_female_data)
#print("Descriptive statistics for Asian/Pacific Islander females:\n", ap_female_data.ESTIMATE.describe().round(2))

"""FEMALES, HISPANIC/LATINO"""
# print("Data for all Hispanic/Latino females:\n", hi_female_data)
# print("Descriptive statistics for all Hispanic/Latino females:\n", hi_female_data.ESTIMATE.describe().round(2))

"""MALES, WHITE, NOT HISPANIC OR LATINO"""
# print("Data for non-Hispanic/Latino White males:\n", wh_nh_male_data)
# print("Descriptive statistics for non-Hispanic/Latino White males:\n", wh_nh_male_data.ESTIMATE.describe().round(2))

"""MALES, BLACK/AFRICAN-AMERICAN, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Black/African-American males:\n", bl_nh_male_data)
# print("Descriptive statistics for non-Hispanic/Latino Black/African-American males:\n", bl_nh_male_data.ESTIMATE.describe().round(2))

"""MALES, NATIVE AMERICAN/ALASKAN, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Native American/Alaskan males:\n", na_nh_male_data)
# print("Descriptive statistics for non-Hispanic/Latino Native American/Alaskan males:\n", na_nh_male_data.ESTIMATE.describe().round(2))

"""MALES, ASIAN/PACIFIC ISLANDER, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Asian/Pacific Islander males:\n", ap_nh_male_data)
# print("Descriptive statistics for non-Hispanic/Latino Asian/Pacific Islander males:\n", ap_nh_male_data.ESTIMATE.describe().round(2))

"""FEMALES, WHITE, NOT HISPANIC OR LATINO"""
# print("Data for non-Hispanic/Latino White females:\n", wh_nh_female_data)
# print("Descriptive statistics for non-Hispanic/Latino White females:\n", wh_nh_female_data.ESTIMATE.describe().round(2))

"""FEMALES, BLACK/AFRICAN-AMERICAN, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Black/African-American females:\n", bl_nh_female_data)
# print("Descriptive statistics for non-Hispanic/Latino Black/African-American females:\n", bl_nh_female_data.ESTIMATE.describe().round(2))

"""FEMALES, NATIVE AMERICAN/ALASKAN, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Native American/Alaskan females:\n", na_nh_female_data)
# print("Descriptive statistics for non-Hispanic/Latino Native American/Alaskan females:\n", na_nh_female_data.ESTIMATE.describe().round(2))

"""FEMALES, ASIAN/PACIFIC ISLANDER, NOT HISPANIC/LATINO"""
# print("Data for non-Hispanic/Latino Asian/Pacific Islander females:\n", ap_nh_female_data)
# print("Descriptive statistics for non-Hispanic/Latino Asian/Pacific Islander females:\n", ap_nh_female_data.ESTIMATE.describe().round(2))

"""MISC"""
#print("Data in single-race rows:\n", sr_data)

"""MALE, COMPARISON BY RACE"""
# print("Descriptive statistics for White males:\n", wh_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Black/African-American males:\n", bl_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Native American/Alaskan males:\n", na_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Asian/Pacific Islander males:\n", ap_male_data.ESTIMATE.describe().round(2))

"""FEMALE, COMPARISON BY RACE"""
# print("Descriptive statistics for White females:\n", wh_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Black/African-American females:\n", bl_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Native American/Alaskan females:\n", na_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for Asian/Pacific Islander females:\n", ap_female_data.ESTIMATE.describe().round(2))

"""MALE, COMPARISON BY RACE AND HISPANIC ORIGIN"""
# print("Descriptive statistics for non-Hispanic/Latino White males:\n", wh_nh_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Black/African-American males:\n", bl_nh_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Native American/Alaskan males:\n", na_nh_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Asian/Pacific Islander males:\n", ap_nh_male_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for all Hispanic/Latino males:\n", hi_male_data.ESTIMATE.describe().round(2))

"""FEMALE, COMPARISON BY RACE AND HISPANIC ORIGIN"""
# print("Descriptive statistics for non-Hispanic/Latino White females:\n", wh_nh_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Black/African-American females:\n", bl_nh_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Native American/Alaskan females:\n", na_nh_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for non-Hispanic/Latino Asian/Pacific Islander females:\n", ap_nh_female_data.ESTIMATE.describe().round(2))
# print("Descriptive statistics for all Hispanic/Latino females:\n", hi_female_data.ESTIMATE.describe().round(2))

# draw plots
plt.show()