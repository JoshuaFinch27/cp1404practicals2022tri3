"""
CP1404 - Practical 4
Program that: prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.

ALSO:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

Program that: Ask the user for their username. If the username is in the above list of
 authorised users, print "Access granted", otherwise print "Access denied".
"""


# Program 1:
def main():
    """Gets numbers from user"""
    numbers = []
    for repetition in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    number_exercises(numbers)


def number_exercises(numbers):
    """Prints the answers to the list exercises"""
    print('The first number is', numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


main()

# Program 2:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

# Small enough that it doesn't need main() function
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
