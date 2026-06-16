## Exercise 6 - skiprows parameter - Skip the first n rows in the file

import pandas as pd

df = pd.read_csv("Data/sales_data_with_stores.csv", skiprows=300)

print(df.shape)