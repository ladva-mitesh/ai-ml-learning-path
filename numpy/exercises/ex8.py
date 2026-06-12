# Exercise 8. How to stack two arrays vertically?
import numpy as np

arr1 = np.arange(10).reshape(2,-1)
arr2 = np.repeat(5,10).reshape(2,-1)

print("arra1: ", arr1)
print("\narra2: ", arr2)

stacked_array = np.vstack([arr1,arr2])

print("\nstacked_array: ", stacked_array)