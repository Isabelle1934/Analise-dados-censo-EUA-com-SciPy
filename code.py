import pandas as pd
import numpy as np
from scipy import stats

c = ("moved_same_state.csv")
v = ("moved_between_states.csv")

control = pd.read_csv(c)
variant = pd.read_csv(v)

# control.head()
# variant.head()

county = pd.DataFrame()
state = pd.DataFrame()
division = pd.DataFrame()
region = pd.DataFrame()

state["Relocated Within State"] = control.groupby("State")["Total Population"].sum()
state["Relocated Between States"] = variant.groupby("State")["Total Population"].sum()

state.head()

cny = state.loc[["California", "New York"]]

cny

t_stat, p_value = stats.ttest_ind(cny["Relocated Within State"], cny["Relocated Between States"])

print("t-statistic:", t_stat)
print("p-value:", p_value)

d = control[(control["State"] == "California") | (variant["State"] == "New York")]

cny2 = pd.DataFrame()
cny2["Total U.S. Citizens (Naturalized)"] = d.groupby("State")["Total US Citizens (Naturalized)"].sum()
cny2["Total Non-Citizens"] = d.groupby("State")["Total Non-Citizens"].sum()

cny2

d = control[(control["State"] == "California") | (variant["State"] == "New York")]

cny2 = pd.DataFrame()
cny2["Total U.S. Citizens (Naturalized)"] = d.groupby("State")["Total US Citizens (Naturalized)"].sum()
cny2["Total Non-Citizens"] = d.groupby("State")["Total Non-Citizens"].sum()

cny2

t_stat, p_value = stats.ttest_ind(cny2["Total U.S. Citizens (Naturalized)"], cny2["Total Non-Citizens"])

print("t-statistic:", t_stat)
print("p-value:", p_value)

cny3 = pd.DataFrame()
cny3["Total U.S. Citizens (Native)"] = d.groupby("State")["Total US Citizens (Native)"].sum()
cny3["Total U.S. Citizens (Naturalized)"] = cny2["Total U.S. Citizens (Naturalized)"]

cny3

t_stat, p_value = stats.ttest_ind(cny3["Total U.S. Citizens (Native)"], cny3["Total U.S. Citizens (Naturalized)"])

print("t-statistic:", t_stat)
print("p-value:", p_value)

region["High School Graduate (or its Equivalency)"] = control.groupby("Region")["High School Graduate (or its Equivalency)"].sum()
region["Bachelor's Degree"] = control.groupby("Region")["Bachelor's Degree"].sum()

nem = region.loc[region.index.isin(["Northeast", "South"])]
# nem

t_stat, p_value = stats.ttest_ind(nem["High School Graduate (or its Equivalency)"], nem["Bachelor's Degree"])

print("t-statistic:", t_stat)
print("p-value:", p_value)

division["Never Married"] = control.groupby("Division")["Never Married"].sum()
division["Married"] = control.groupby("Division")["Married"].sum()

sam = division.loc[division.index.isin(["South Atlantic", "Mountain"])]
# sam

t_stat, p_value = stats.ttest_ind(sam["Never Married"], sam["Married"])

print("t-statistic:", t_stat)
print("p-value:", p_value)

county["Never Married"] = control.groupby("County")["Never Married"].sum()
county["Married"] = control.groupby("County")["Married"].sum()

# home = county.loc[county.index.isin(["Your Home county", "Home County 2"])]

