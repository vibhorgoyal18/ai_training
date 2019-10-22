# Find the difference, using difference and symmetric_difference, between two given lists - list1 and list2.
# First, convert the lists into sets and store them as set_1 and set_2.
# Then store the difference and symmetric difference in answer_1 and answer_2 respectively.
# Print both the answers as sorted lists, i.e. convert the final sets to lists, sort it and then return it.


input_list = [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7, 8, 9]]
list_1 = input_list[0]
list_2 = input_list[1]

set_1 = set(list_1)
set_2 = set(list_2)
answer_1 = set_1.difference(set_2)
answer_2 = set_1.symmetric_difference(set_2)

print(list(answer_1))
print(list(answer_2))
