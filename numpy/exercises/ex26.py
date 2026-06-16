# Exercise 26. How to extract a particular column from 1D array of tuples?

import numpy as np

data = np.genfromtxt("Data/Iris.csv", delimiter=",", usecols=[-1], dtype=object)

print(data)