import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

pd = pa.read_csv("suicide_by_state.csv")

q_low = pd["percent_change"].quantile(0.01)
q_hi  = pd["percent_change"].quantile(0.99)

pd = pd[(pd["percent_change"] < q_hi) & (pd["percent_change"] > q_low)]

features = pd["percent_change"].astype('float')
labels = pd["rank"].astype('float')

print(features)
print(labels)

slope, intercept, r, p, std_err = stats.linregress(features, labels)

def lineFunc(x):
  return slope * x + intercept

lineY = list(map(lineFunc, features))
print(lineY)

plot.scatter(features,labels)
plot.plot(features,lineY)
plot.show()

print("Regression Predictions (Percent Change in Suicide Rate between 2019 and 2020) by Lockdown Severity Rank:")

distinct_age_groups = sorted(list(set(labels)))
for age_group in distinct_age_groups:
  prediction = lineFunc(age_group)
  print(str(age_group) + ": " + str(prediction))