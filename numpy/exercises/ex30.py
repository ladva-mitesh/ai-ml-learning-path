"""
SOFTMAX ON THE IRIS DATASET
===========================

Objective
---------
Compute the Softmax scores of the Sepal Length values in the Iris dataset.

Theory
------
Softmax is a function that converts a list of numerical values into a
probability distribution.

Formula:

                e^(x_i)
P(x_i) = ------------------------
                Σ e^(x_j)

where:
- x_i is the current value
- e ≈ 2.71828 (Euler's number)
- Σ means sum of all exponentials

Properties
----------
1. Every output value is positive.
2. All output values sum to 1.
3. Larger input values receive larger probabilities.
4. Commonly used in Machine Learning classification problems.

Example
-------
Input:

[5, 6, 7]

Step 1: Compute exponentials

[e^5, e^6, e^7]

=
[148.41, 403.43, 1096.63]

Step 2: Compute total

148.41 + 403.43 + 1096.63

=
1648.47

Step 3: Normalize

[148.41/1648.47,
 403.43/1648.47,
1096.63/1648.47]

Result:

[0.09, 0.24, 0.67]

Interpretation
--------------
The largest value receives the largest probability.

About This Exercise
-------------------
This exercise does NOT perform classification.

Instead, it treats every Sepal Length value as a score and applies the
Softmax function to convert the entire Sepal Length column into a
probability distribution.

Expected Result
---------------
- softmax.sum() should be approximately 1.
- Larger Sepal Length values will have larger Softmax scores.
"""

import numpy as np

iris_data = np.genfromtxt(
    'Data/Iris.csv',
    delimiter=',',
    dtype='float',
    usecols=[1],
    skip_header=1
)

softmax = np.exp(iris_data) / np.sum(np.exp(iris_data))

print("Sum of Softmax values:")
print(softmax.sum())

print("\nSoftmax Scores:")
print(softmax)