# From a 2D array extract all the rows of the 2 column.
# Hint: 2 column will have index value as 1.
import numpy as np

input_list = [[5, 6, 7], [7, 6, 5], [0, 8, 7]]
array_2d = np.array(input_list)
print(array_2d[:, 1])
