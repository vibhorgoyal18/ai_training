# Angle Between Emails
# The frequency table of words in four sample emails is shown below. The angle between emails 1 and 2 is (the first two rows):
#
# money	hurry	meeting	powerpoint
# 2	1	0	0
# 0	0	1	1
# 1	1	0	0
# 1	1	1	0
import math
import numpy as np

v1 = np.array([2, 1, 0, 0])
v2 = np.array([0, 0, 1, 1])
v3 = np.array([1, 1, 0, 0])
v4 = np.array([1, 1, 1, 0])
pi = math.pi
print("v1-v2: " + str(np.arccos(0 / (np.sqrt(5) * np.sqrt(2))) * (180 / pi)))
print("v1-v3: " + str(np.arccos(3 / (np.sqrt(5) * np.sqrt(2))) * (180 / pi)))
print("v1-v4: " + str(np.arccos(3 / (np.sqrt(5) * np.sqrt(3))) * (180 / pi)))
print("v3-v4: " + str(np.arccos(2 / (np.sqrt(2) * np.sqrt(3))) * (180 / pi)))
