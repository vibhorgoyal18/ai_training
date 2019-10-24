# Horizontally stack two arrays using hstack, and finally, vertically stack the resultant array with the third array.
#
# Example:
# Input 1:
# [[1, 2],
#  [5, 6]]
#
# [[3, 4],
#  [7, 8]]
#
# [[9, 10, 11, 12]]
# Output 1:
# [[1 2 3 4]
#  [5 6 7 8]
#  [9 10 11 12]]

import numpy as np

input_list = [[[1, 2], [5, 6]], [[3, 4], [7, 8]], [[9, 10, 11, 12]]]
list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

horizontal_stack = np.hstack((list_1, list_2))
vertical_stack = np.vstack((horizontal_stack, list_3))

print(vertical_stack)
