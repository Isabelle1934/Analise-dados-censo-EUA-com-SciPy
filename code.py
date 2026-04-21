import pandas as pd
import numpy as np
from scipy import stats

c = ("/content/moved_same_state.csv")
v = ("/content/moved_between_states.csv")
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
