# Perform an element-wise multiplication using list_1 = [2,3,4,5] list_2 = [7,8,9,6] and obtain the output as a list.
# Hint: Convert the list to an array and after multiplication convert it back to a list.

import numpy as np

list_1 = [2, 3, 4, 5]
list_2 = [7, 8, 9, 6]

array_1 = np.array(list_1)
array_2 = np.array(list_2)
array_3 = array_1 * array_2

print(list(array_3))
