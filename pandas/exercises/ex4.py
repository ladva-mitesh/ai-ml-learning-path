## Exercise 4 - usecols parameter 

import pandas as pd

df = pd.read_csv("Data/file_with_many_columns.csv", usecols=range(10))

print(df.head(3))