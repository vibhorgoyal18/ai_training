# Create a lambda function 'greater', which takes two arguments x and y and return x if x>y otherwise y.
# If x = 2 and y= 3, then the output should be 3.

a = 2
b = 3

greater = lambda x, y: x if x > y else y

print(greater(a, b))
