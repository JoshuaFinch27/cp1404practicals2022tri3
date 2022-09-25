"""
CP1404 - Practical 2
Program to ask user for a password with error checking
"""

MINIMUM_LENGTH = 6


def main():
    """Asks user for a password with error checking"""
    password = get_password()
    while len(password) < MINIMUM_LENGTH:
        print("Invalid - Password is too short.")
        password = get_password()
    print_password_as_stars(password)


def print_password_as_stars(password):
    print(len(password) * "*")


def get_password():
    """Function gets password input from user"""
    password = str(input("Password: "))
    return password


main()
