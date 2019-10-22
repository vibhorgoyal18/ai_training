# From a Dictionary input_dict={'Name': 'Monty', 'Profession': 'Singer' },
# get the value of a key ‘Label’ which is not a part of the dictionary,
# in such a way that Python doesn't hit an error. If the key does not exist in the dictionary,
# Python should return 'NA'.


input_dict = {'Name': 'Monty', 'Profession': 'Singer'}

answer = input_dict.get('Label', 'NA')
print(answer)
