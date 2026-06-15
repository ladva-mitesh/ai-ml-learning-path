# Exercise 17. How to swap two rows in a 2d numpy array?

import numpy as np

arr1 = np.arange(9).reshape(3,3)

print('Original array\n', arr1)
print('\nModified array\n', arr1[[0,2,1],:])