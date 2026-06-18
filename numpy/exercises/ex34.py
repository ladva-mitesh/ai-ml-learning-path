# Exercise 34. How to filter a numpy array based on two or more conditions?

# Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

import numpy as np

iris_data = np.genfromtxt(
    'Data/Iris.csv',
    delimiter=',',
    dtype='float',
    usecols=[1,2,3,4],
    skip_header=1
)

filtered_data = iris_data[(iris_data[:, 2] > 1.5) & (iris_data[:,0] < 5.0)]

print(filtered_data)