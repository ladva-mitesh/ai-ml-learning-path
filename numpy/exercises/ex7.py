# Exercise 7. How to reshape an array?

import numpy as np

arr = np.arange(10)
reshaped_arr = arr.reshape((5,-1))

print("\n Original array:", arr)
print("\n Reshaped array:", reshaped_arr)