# Solve the following system of three equations and three unknowns in Numpy and report the solution:
#
# 2x + 6y -z = 0
# x + 2y - 2z = 1
# -5x + 2z = 8

import numpy as np

a = np.array([[2, 6, -1],
              [1, 2, -2],
              [-5, 0, 2]])

b = np.array([0, 1, 8])

# compute the inverse
A_inv = np.linalg.inv(a)

# solution: A_inv * b
x = np.dot(A_inv, b)
print(x)
