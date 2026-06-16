## Exercise 1 - display first n rows

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")
n = 5

print(df.head(n))