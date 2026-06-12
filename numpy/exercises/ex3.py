# Exercise 3. How to create a boolean array?
import numpy as np

arr1 = np.full((3,3), False, dtype=bool)
# Create a 3×3 numpy array of all True’s
arr2 = np.full((3,3), True, dtype=bool)

arr3 = np.full((9), True, dtype=bool).reshape((3,-1))

print(arr1)
print(arr2)
print(arr3)