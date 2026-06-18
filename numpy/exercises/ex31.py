# A percentile is the value below which a given percentage of the data falls.

# Examples

# 5th percentile = 4.6 → 5% of the values are less than or equal to 4.6.
# 50th percentile → 50% of the values are less than or equal to this value (the median).
# 95th percentile = 7.255 → 95% of the values are less than or equal to 7.255.

# Easy way to remember

# Percentile = "What value has X% of the data below it?"

# Exercise 31. How to find the percentile scores of a numpy array? - Find the 5th and 95th percentile of iris's sepallength

import numpy as np

iris_data = np.genfromtxt("Data/Iris.csv", delimiter=",", skip_header=True, dtype=float, usecols=[1])

percentile_result = np.percentile(iris_data, q=[5,95])
print(percentile_result)
print(iris_data.size)
print((iris_data <= percentile_result[0]).sum())
print((iris_data <= percentile_result[1]).sum())