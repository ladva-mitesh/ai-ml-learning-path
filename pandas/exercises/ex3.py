## Exercise 3 - usecols parameter

import pandas as pd

column_list = ["store","product_code","cost","price"]

df = pd.read_csv("Data/sales_data_with_stores.csv", usecols=column_list)

print(df.head())