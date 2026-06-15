# Exercise 18. How to reverse the rows of a 2D array?

import numpy as np

arr1 = np.arange(9).reshape(3,3)

print('Original array\n', arr1)

print('\nModified array\n', arr1[::-1,:])