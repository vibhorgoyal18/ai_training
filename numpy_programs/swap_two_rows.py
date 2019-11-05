# Given m and n, swap the mth and nth rows of the 2-D NumPy array given below.
#
# a = [[4 3 1]
#          [5 7 0]
#          [9 9 3]
#          [8 2 4]]
#
# Example:
# Input 1:
# 0
# 2
# Output 1:
# [[9 9 3]
#  [5 7 0]
#  [4 3 1]
#  [8 2 4]]

import numpy as np

# Given array
a = np.array([[4, 3, 1],
              [5, 7, 0],
              [9, 9, 3],
              [8, 2, 4]])

# Read the values of m and n

m = 0
n = 1

a[[m, n]] = a[[n, m]]
print(a)
