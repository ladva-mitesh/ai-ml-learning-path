import numpy as np

A = np.array([[2,0],[0,3]])

eigen_values, eigen_vectors = np.linalg.eig(A)

# print("Eigen values of A", eigen_values)
# print("\nEigen vectors of A", eigen_vectors)

B = np.array([[-2,0],[0,3]])

eigen_values, eigen_vectors = np.linalg.eig(B)

# print("Eigen values of B", eigen_values)
# print("\nEigen vectors of B", eigen_vectors)

# Diagnolisation

C = np.array([[4,1], [2,3]])
eigen_values, eigen_vectors = np.linalg.eig(C)

# print("Eigen values of B", eigen_values)
# print("\nEigen vectors of B", eigen_vectors)

# Formula: C = PDP^-1

p = eigen_vectors
d = np.diag(eigen_values)
p_inv = np.linalg.inv(eigen_vectors)

# print("\np: ",p)
# print("\nd: ",d)
# print("\np_inv: ",p_inv)

c_power_20 = p @ np.linalg.matrix_power(d,20) @ p_inv

print(np.linalg.matrix_power(C,20))
print(c_power_20)