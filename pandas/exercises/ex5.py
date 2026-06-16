## Exercise 5 - nrows parameter

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv", nrows=250)

print(df.shape)