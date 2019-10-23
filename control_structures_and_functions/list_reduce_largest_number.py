# You are given a list of numbers such as input_list = [31, 63, 76, 89].
# Find and print the largest number in input_list using the reduce() function.

from functools import reduce

input_list = [31, 63, 76, 89]
answer = reduce(lambda x, y: x if x > y else y, input_list)
print(answer)
