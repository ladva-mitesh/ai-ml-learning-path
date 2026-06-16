# Exercise 23. How to limit the number of items printed in output of numpy array?

import numpy as np

arr = np.arange(99)

print("Before:")
print(arr)

np.set_printoptions(threshold=6)

print("\nAfter:")
print(arr)