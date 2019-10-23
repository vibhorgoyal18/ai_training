# Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively.
# For e.g. if the input list is:
# [ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
# the output list should be the list:
# ['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']
# Note: Add a space between first name and last name.

input_list = [['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
first_name = input_list[0]
last_name = input_list[1]

name = list(map(lambda first, last: first + ' ' + last, first_name, last_name))

print(name)
