# Given an array, 'array_3' divide each element with 5.
# Hint: Create a vectorized function, then apply it to the array_3

import numpy as np

input_list = [[1, 2, 3, 4], [4, 7, 5, 6], [9, 0, 7, 8], [6, 7, 8, 5]]
list_1 = input_list[0:2]
list_2 = input_list[2:4]

array_1 = np.array(list_1)
array_2 = np.array(list_2)
array_3 = np.hstack((array_1, array_2))

function = np.vectorize(lambda x: x / 5)

print(function(array_3))
