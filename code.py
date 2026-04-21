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
