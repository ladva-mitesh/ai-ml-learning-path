## Exercise 8 - describe function - Customize percentiles

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.describe(percentiles=[0.1, 0.9]))