# Exercise 10. How to generate custom sequences in numpy without hardcoding?
# imput: [1, 2, 3]
#output: [1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3]

import numpy as np

a = np.array([1, 2, 3])
# print(a) -> [1 2 3]
b = np.repeat(a,3)
# print(b) -> [1 1 1 2 2 2 3 3 3]
c = np.tile(a,3)
# print(c) -> [1 2 3 1 2 3 1 2 3]
result = np.hstack([b,c])
print(result)
# print(result2)
result2 = np.r_[b,c] # alternate way of concatenate two arrays