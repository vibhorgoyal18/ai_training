# Given a single integer n, create an (n x n) 2D array with 1 on the border and 0 on the inside.
#
# Note: Make sure the array is of type int.
#
# Example:
# Input 1:
# 4
# Output 1:
# [[1 1 1 1]
# [1 0 0 1]
# [1 0 0 1]
# [1 1 1 1]]
# Input 2:
# 2
# Output 2:
# [[1 1]
#  [1 1]]

import numpy as np

n = int(input('Enter a number: '))

a = np.ones((n, n), dtype=int)
a[1:-1, 1:-1] = 0
print(a)
