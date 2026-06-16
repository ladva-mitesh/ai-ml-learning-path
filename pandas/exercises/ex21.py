## Exercise 10 - describe function - For columns with object data type

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.describe(include=[object]))