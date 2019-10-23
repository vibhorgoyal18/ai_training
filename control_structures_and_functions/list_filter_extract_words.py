# You are given a list of strings such as input_list =  ['hdjk', 'salsap', 'sherpa'].
# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
# Note: Use the filter() function.

input_list = ['hdjk', 'salsap', 'sherpa']

sp = list(filter(lambda x: x[0] is 's' and x[len(x) - 1] is 'p', input_list))

print(sp)
