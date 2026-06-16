# Exercise 24. How to print the full numpy array without truncating

import numpy as np

arr = np.arange(10000)

print("Before:")
print(arr)

np.set_printoptions(threshold=len(arr))

# np.set_printoptions(threshold=np.inf)

print("\nAfter:")
print(arr)