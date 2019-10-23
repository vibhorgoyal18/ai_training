# Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] using list comprehensions.

input_list = ['wood', 'old', 'apple', 'big', 'item', 'euphoria']

list_vowel = [word for word in input_list if word[0].lower() in ['a','e','i','o','u']]

print(list_vowel)