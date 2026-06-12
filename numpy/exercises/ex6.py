# Exercise 6. How to replace items that satisfy a condition without affecting the original array?

import numpy as np

original_arr = np.arange(10)

outer_arr = original_arr.copy()

outer_arr[outer_arr%2 == 1] = -1

print('Modified Array', outer_arr)
print('\nOriginal Array',original_arr)