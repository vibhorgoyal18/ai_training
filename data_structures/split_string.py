# Split the string input_str = 'Kumar_Ravi_003' to the person's second name, first name and unique customer code.
# In this example, second_name= 'Kumar', first_name= 'Ravi', customer_code = '003'.

input_str = 'Kumar_Ravi_003'
first_name = input_str.split('_')[1]
second_name = input_str.split('_')[0]
customer_code = input_str.split('_')[2]
print(first_name)
print(second_name)
print(customer_code)