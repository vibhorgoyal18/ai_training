# Create an array using list list_1 = [10,11,12,13] and list_2 = [15,12,13,14] and print the shape and dimension of the array created.

import numpy as np

list_1 = [10, 11, 12, 13]
list_2 = [15, 12, 13, 14]

array_1 = np.array([list_1, list_2])

print(array_1.shape)
print(array_1.ndim)
