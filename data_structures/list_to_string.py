# Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’.
# The sample output of this string will be:
# Pythons syntax is easy to learn & Pythons syntax is very clear
#
# Note that there is a space on both sides of '&' (as usual in English sentences).

input_str = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']

string_1 = ' & '.join(input_str)

print(string_1)
