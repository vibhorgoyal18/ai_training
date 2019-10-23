# You are given an integer input n.
# Write a program to generate a dictionary that contains the key-value pairs
# i: i**2 where ' i ' is an integer number from 1 to n (both 1 and n included).
# For example, if the input is n=8, the output should be a dictionary as follows:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("Enter a positive integer: "))

dictionary = {num: num ** 2 for num in range(1, n + 1)}
print(dictionary)
