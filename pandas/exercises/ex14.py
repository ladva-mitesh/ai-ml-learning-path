## Exercise 2 - display last n rows

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")
n = 5
print(df.tail(n))