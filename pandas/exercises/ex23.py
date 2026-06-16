## Exercise 11 - memory usage - The memory_usage function returns memory usage in bytes

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(df.memory_usage())

print("\n",df.memory_usage().sum())