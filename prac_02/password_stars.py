"""
CP1404 - Practical 2
Program to ask user for a password with error checking
"""

MINIMUM_LENGTH = 6

password = str(input("Password: "))
while len(password) < MINIMUM_LENGTH:
    print("Invalid - Password is too short.")
    password = str(input("Password: "))
print(len(password) * "*")
