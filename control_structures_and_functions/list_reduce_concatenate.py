# Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
# If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.
from functools import reduce

input_list = ['I', 'Love', 'Python']
output = reduce(lambda x, y: x + ' ' + y, input_list)
print(output)
