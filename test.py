import numpy as np

array_2d = np.array([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]])
col_first = array_2d[:, 0]
row_first = array_2d[0, :]
col_last = array_2d[:, array_2d.shape[1] - 1]
row_last = array_2d[array_2d.shape[0] - 1, :]

print(col_first)
print(row_first)
print(col_last)
print(row_last)
