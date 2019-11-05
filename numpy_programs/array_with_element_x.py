# Given an integer 'x', create an array of size m*n having all integer values equal to 'x'.
# Hint: Use dtype to specify integer.
#
# Format:
# Input:
# Line 1: A single integer 'x'
# Line 2: A single integer 'm' indicating the number of rows
# Line 3: A single integer 'n' indicating the number of columns
# Output: An array of size 'm*n' having all the values as 'x'
#
# Example:
# Input 1:
# 1
# 3
# 3
# Output 1:
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

import numpy as np

int_x = int(input('Enter the integer value: '))
rows_m = int(input('Enter the number of rows: '))
cols_n = int(input('Enter the number of columns: '))


# Create an array of m*n with all elements equal to 'x' using the tile() function
array_x = np.tile(int_x, (rows_m, cols_n))

# Print the created array
print(array_x)

# Alternatively
# Create an array of m*n with all elements equal to '1' using the ones() function
# and multiply it by 'x'.
array_x = int_x * np.ones((rows_m, cols_n), dtype=np.int)
