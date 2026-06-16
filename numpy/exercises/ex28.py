# Exercise 28. How to compute the mean, median, standard deviation of a numpy array?

import numpy as np

iris_data = np.genfromtxt("Data/Iris.csv", delimiter=",", skip_header=True, usecols=[1])

print(iris_data)

print("\nMean", np.mean(iris_data))
print("Median", np.median(iris_data))
print("Standard Deviation", np.std(iris_data))