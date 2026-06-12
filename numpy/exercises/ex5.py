# Exercise 5. How to replace items that satisfy a condition with another value in numpy array?

import numpy as np

arr = np.arange(10)
print(f"Original array: {arr}")
arr[arr>3] = -1
print(f"After modification array: {arr}")