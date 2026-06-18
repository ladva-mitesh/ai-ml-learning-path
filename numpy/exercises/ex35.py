# Exercise 35. How to drop rows that contain a missing value from a numpy array?

import numpy as np

# arr = np.array([
#     [1, 2, 3],
#     [4, np.nan, 6],
#     [7, 8, 9],
#     [1, 2, 3],
#     [4, np.nan, 6],
#     [7, 8, 9],
#     [1, 2, 3],
#     [4, np.nan, 6],
#     [7, 8, 9],
#     [1, 2, 3],
#     [4, np.nan, 6],
#     [7, 8, 9],
#     [1, 2, 3],
#     [4, np.nan, 6],
#     [7, 8, 9]
# ])

# mask = np.isnan(arr)

# print(arr[np.sum(mask, axis=1) == 0][:5])

diabetes_data = np.genfromtxt('Data/diabetes.csv', delimiter=',', dtype='float', usecols=[0,1,2,3,4,5,6,7], skip_header=1)
diabetes_data[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

print(diabetes_data[np.sum(np.isnan(diabetes_data), axis=1) == 0][:5])