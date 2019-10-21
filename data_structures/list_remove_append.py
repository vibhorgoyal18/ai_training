# Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.

input_list = ['SAS', 'R', 'PYTHON', 'SPSS']
input_list.remove('SPSS')
input_list.append('SPARK')
print(input_list)