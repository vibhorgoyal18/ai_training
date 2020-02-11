import numpy as np

A = np.array([[4, 9],
              [7, 6]])

# c is the array of eigenvalues
# v is the matrix with eigenvectors as the columns
c, v = np.linalg.eig(A)
print(c)
print(v)