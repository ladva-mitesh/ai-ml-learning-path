## Exercise 4 - columns

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.columns)
print("\n",list(df.columns))