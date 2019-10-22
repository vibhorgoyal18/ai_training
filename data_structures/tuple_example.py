# Add the element ‘Python’ to a tuple input_tuple = ('Monty Python', 'British', 1969).
# Since tuples are immutable, one way to do this is to convert the tuple to a list, add the element,
# and convert it back to a tuple.

input_tuple = ('Monty Python', 'British', 1969)

list_1 = list(input_tuple)
list_1.append('Python')
tuple_2 = tuple(list_1)
print(tuple_2)
