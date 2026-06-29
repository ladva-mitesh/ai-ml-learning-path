import numpy as np

# Sample Data
# User Movie1 Movie2 Movie3
# A    5      4       0
# B    4      5       0
# C    1      0       5

ratings = np.array([
    [5,4,0],
    [4,5,0],
    [1,0,5],
])

u, s, vt = np.linalg.svd(ratings)

print(u @ np.diag(s) @ vt)
