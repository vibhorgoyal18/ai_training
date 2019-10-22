# Create a SORTED list of all values from the dictionary
# input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

input_dict = {'Jack Dorsey': 'Twitter', 'Tim Cook': 'Apple', 'Jeff Bezos': 'Amazon', 'Mukesh Ambani': 'RJIO'}

value_list = list(input_dict.values())
print(sorted(value_list))
