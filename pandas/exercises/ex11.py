## Exercise 11 - to_csv function - If you don't want pandas to save its DataFrame index as an extra CSV column, use index=False when calling to_csv().

import pandas as pd

df = pd.read_csv("Data/sample_dataset.csv")

df.to_csv("Data/sample_dataset_2.csv", index=False)

df = pd.read_csv("Data/sample_dataset_2.csv")

print(df)