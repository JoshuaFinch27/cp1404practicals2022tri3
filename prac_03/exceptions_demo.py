"""
CP1404 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
    -> When a non integer number is entered by the user.
2. When will a ZeroDivisionError occur?
    -> When the user enters '0' as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    -> Yes, by adding a function that checks if a number is valid -> if it isn't then it asks again
       instead of ending the program
"""


def main():
    """"""
    numerator = get_valid_number("Enter the numerator: ")
    denominator = get_valid_number("Enter the denominator: ")
    fraction = numerator / denominator
    print(f"{fraction} \nFinished")


def get_valid_number(text):
    """Gets valid numbers from the user"""
    try:
        number = int(input(text))
        while number == 0:
            print("Any fraction that has zero as the numerator is equal to zero.\nYou also cannot divide by zero.")
            number = int(input(text))
        return number
    except ValueError:
        print("Numerator and denominator must be valid numbers!")


main()
