# Exercise 25. How to import a dataset with numbers and texts keeping the text intact in python numpy?

import numpy as np

iris_data = np.genfromtxt(
    "Data/iris.csv", 
    delimiter=",",
    skip_header=True,
    usecols=[0],
    max_rows=2,
    dtype=object
)

print(iris_data)