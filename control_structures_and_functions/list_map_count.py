# Using the function Map, count the number of words that start with ‘S’ in input_list.

input_list = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']

count = sum(list(map(lambda str: 1 if str[0] is 'S' else 0, input_list)))

print(count)
