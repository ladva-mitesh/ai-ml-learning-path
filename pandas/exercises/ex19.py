## Exercise 7 - describe function

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.describe()) # gives you a statistical summary of all numeric columns.