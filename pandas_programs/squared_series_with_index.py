# Create
# a
# panda
# series
# that
# contains
# the
# first ‘n’ natural
# numbers and their
# respective
# squares.The
# first ‘n’ numbers
# should
# appear in the
# index
# position.
# Hint: Use
# manual
# indexing.
#
# Format:
# Input: A
# natural
# number
# 'n'
# Output: A
# pandas
# series
# with the first 'n' natural numbers in the index position and their respective squares in the adjacent column.
#
# Example:
# Input
# 1:
# 4
# Output
# 1:
# 1
# 1
# 2
# 4
# 3
# 9
# 4
# 16
# dtype: int64


import numpy as np
import pandas as pd

n = int(input("Enter a number: "))

series = pd.Series(np.array(range(1, n + 1)) ** 2, index=range(1, n + 1))
print(series)
