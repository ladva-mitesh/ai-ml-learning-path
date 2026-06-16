# Exercise 22. How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?

import numpy as np

np.random.seed(100)

rand_arr = np.random.random((3,3)) / 1e6

print("Before:")
print(rand_arr)

np.set_printoptions(suppress=True)

print("\nAfter:")
print(rand_arr)