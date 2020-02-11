# Calculating Dot Product
# Description
# Let's look at some code. Find the dot product between the following two vectors:
# a = (3, 4, 5)
# b = (1, 3, 5)
#
# We've pre-written the code needed to calculate the dot product.
# You just need to type in these vectors (inside the square bracket), and hit Run.
#
# Also, calculate this value by hand. Does the output of the code match your value?

import numpy as np

a = np.array([3, 4, 5])
b = np.array([1, 3, 5])

print(np.dot(a, b))
