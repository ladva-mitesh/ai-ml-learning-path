# Exercise 33. How to find the position of missing values in numpy array?

import numpy as np

# arr = np.array([10, 20, np.nan, 40, np.nan, 60])

# print(np.isnan(arr))
# print(np.where(np.isnan(arr)))

iris_data = np.genfromtxt(
    'Data/Iris.csv',
    delimiter=',',
    dtype='float',
    usecols=[1,2,3,4],
    skip_header=1
)

np.random.seed(50)

iris_data[ np.random.randint(len(iris_data), size=20), np.random.randint(4, size=20) ] = np.nan

# Find total mising value in complete data
print("Number of missing values in Iris data: \n", np.isnan(iris_data).sum())

# Find total mising value in 1D data
print("Number of missing values in any one feature of Iris data: \n",np.isnan(iris_data[:,1]).sum())

print("Position of missing values in any one feature of Iris data:: \n", np.where(np.isnan(iris_data[:, 1])))