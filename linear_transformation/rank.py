# Consider the following system of three equations and three variables:
#
# 2x - y - z = 1
#
# 2x - y +z = 0
#
# 4x - 2y - 3z = -1
#
# The system of equations (hint: look at the determinant of the matrix A using np.linalg.det(A):

import numpy as np

A = np.array([[2, -1, -1],
              [2, -1, 1],
              [4, -2, -3]])

B = np.array([1, 0, -1])

C = np.array([[1, 3], [2, 6]])

print(np.linalg.matrix_rank(A))
