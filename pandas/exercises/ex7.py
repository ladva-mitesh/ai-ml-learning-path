## Exercise 7 - skiprows parameter

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv", skiprows=lambda x: x % 2 == 1)

print(df.shape)