## Exercise 9 - parse_dates
# - Can convert the data type after reading the data. 
# - Another option is to handle this task while reading the data.

import pandas as pd

df = pd.read_csv("Data/prices.csv", parse_dates=['date'])

print(df.dtypes)