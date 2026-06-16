# Exercise 27. How to convert a 1d array of tuples to a 2d numpy array?
# corrected title : How to load selected numeric columns from a CSV file into a 2D NumPy array?

import numpy as np

iris_data = np.genfromtxt("Data/Iris.csv", delimiter=",", skip_header=True, dtype=object, usecols=[0,1,2,3])

print(iris_data)