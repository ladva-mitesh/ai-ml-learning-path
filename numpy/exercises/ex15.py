# Exercise 15. How to make a python function that handles scalars to work on numpy arrays?

import numpy as np

maxx = lambda x, y: x if x>= y else y

def pair_max(x, y):
    maximum = [maxx(a,b) for a,b in zip(x,y)]
    # maximum = [maxx(a,b) for a,b in map(lambda a,b:(a,b),x,y)]
    return np.array(maximum)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(a, b))