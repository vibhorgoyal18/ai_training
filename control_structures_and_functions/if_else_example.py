# Write a code to check if the string in input_str starts with a vowel or not. Print capital YES  or NO.
# For example, if input_str = 'analytics' then, your output should print 'YES'.

input_str = 'analytics'

if input_str[0] in ('a','e','i','o','u'):
    print('YES')
else:
    print('NO')