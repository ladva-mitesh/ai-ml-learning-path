# Exercise 32. How to insert values at random positions in an array?

import numpy as np

iris_data = np.genfromtxt(
    'Data/Iris.csv',
    delimiter=',',
    dtype='float',
    usecols=[1,2,3,4],
    skip_header=1
)

random_raw_arr = np.random.randint(0, iris_data.shape[0], 20)
random_column_arr = np.random.randint(0, iris_data.shape[1], 20)

iris_data[random_raw_arr, random_column_arr] = np.nan

print(iris_data)