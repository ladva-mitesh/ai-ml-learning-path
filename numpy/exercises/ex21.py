# Exercise 21. How to print only 3 decimal places in python numpy array?
import numpy as np

rand_arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print(rand_arr)