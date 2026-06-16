## Exercise 11 - describe function - Include only floats

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.describe(include=float))