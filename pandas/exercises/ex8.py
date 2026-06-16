## Exercise 8 - index_col parameter -  Use a specific column as the index in the DataFrame

import pandas as pd

df = pd.read_csv("Data/prices.csv", index_col="product_id")

print(df.head())