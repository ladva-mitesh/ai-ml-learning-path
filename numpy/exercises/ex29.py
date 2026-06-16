# Exercise 29. How to normalize an array so the values range exactly between 0 and 1?

# Normalize : Bring values to a common scale without changing their relative relationships. The formula is: (x-min)/(max-min)

import numpy as np

arr = np.array([10, 20, 30, 40, 50], dtype=int)

print((arr-np.min(arr))/(np.max(arr)-np.min(arr)))

iris_data = np.genfromtxt("Data/Iris.csv", delimiter=",", skip_header=True, usecols=[1])

print((iris_data)-np.min(iris_data)/np.max(iris_data)-np.min(iris_data))