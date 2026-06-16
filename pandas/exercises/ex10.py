## Exercise 10 - na_values parameter - allows you to specify custom strings, numbers, or lists of values that should be recognized as missing data (NaN)

import pandas as pd

df = pd.read_csv("Data/sample_dataset.csv", na_values=['?'])

print(df)