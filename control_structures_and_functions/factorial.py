# Given a number ‘n’, output its factorial using reduce().
# Note: Make sure you handle the edge case of zero. As you know, 0! = 1
#
# P.S.: Finding the factorial without using the reduce() function might lead to deduction of marks.
#
# Examples:
# Input 1:
# 1
# Output 1:
# 1
#
# Input 2:
# 3
# Output 2:
# 6

from functools import reduce

n = int(input())
factorial = reduce(lambda x, y: 1 if x == 0 else x * y, range(0, n + 1))
print(factorial)
