# Exercise 12. How to remove from one array those items that exist in another?
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

print(np.setdiff1d(a,b))