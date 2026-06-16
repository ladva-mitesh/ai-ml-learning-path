## Exercise 3 - size

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv")

print(f"shape: {df.shape}") # (rows, columns)
print(f"size: {df.size}") # Returns the total number of values (cells) in the DataFrame.
print(f"len: {len(df)}") # Returns the number of rows.