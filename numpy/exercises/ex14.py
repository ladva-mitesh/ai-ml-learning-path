# Exercise 14. How to extract all numbers between a given range from a numpy array?

import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

# Get me all items between 5 to 10

print(a[(a >= 5) & (a <= 10)])