"""
CP1404 - Practical 1
Loops
"""

# a)
for number in range(1, 21, 2):
    print(number, end=' ')
print()

# b)
for number in range(0, 101, 10):
    print(number, end=' ')
print()

# c)
for number in range(20, 0, -1):
    print(number, end=' ')
print()

# d)
number_of_stars = int(input("Enter number of stars: "))
for number in range(number_of_stars):
    print('*', end=' ')
print()

# e)
for number in range(1, number_of_stars +1):
    print('*' * number)
print()
