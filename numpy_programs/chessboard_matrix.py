# Given
# an
# even
# integer ‘n’, create
# an ‘n * n’ checkerboard
# matrix
# with the values 0 and 1, using the tile function.
#
# Format:
# Input: A
# single
# even
# integer
# 'n'.
# Output: An
# 'n*n'
# NumPy
# array in checkerboard
# format.
#
# Example:
# Input
# 1:
# 2
# Output
# 1:
# [[0 1]
#  [1 0]]
# Input
# 2:
# 4
# Output
# 2:
# [[0 1 0 1]
#  [1 0 1 0]
# [0
# 1
# 0
# 1]
# [1 0 1 0]]
import numpy as np

n = int(input("Enter the number of rows of matrix: "))

a = np.resize([0, 1], n)
m = np.abs(a - np.array([a]).T)

print(m)
