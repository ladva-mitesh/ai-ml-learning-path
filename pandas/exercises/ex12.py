## Exercise 12 - read_clipboad

import pandas as pd

df = pd.read_clipboard()

df.to_csv("Data/copied_data.csv", index=False)