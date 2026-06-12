# Exercise 9. How to stack two arrays horizontally?
import numpy as np

arr1 = np.arange(10).reshape(-1,2)
arr2 = np.repeat(1,10).reshape(-1,2)

print("arra1: ", arr1)
print("\narra2: ", arr2)

stacked_array = np.hstack([arr1, arr2])

print("\nstacked_array: ", stacked_array)