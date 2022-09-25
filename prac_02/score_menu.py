"""
CP1404 - Practical 2
Program that: gets valid score, prints result, prints stars as score and quits
"""

MENU = """G - Get valid score
R - Print result
S - Print stars
Q - Quit"""


def main():
    """Score validator, reviewer and viewer"""
    valid_score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            valid_score = get_valid_score()
        elif choice == "R":
            print_score_status(valid_score)
        elif choice == "S":
            print_line_as_stars(valid_score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def get_valid_score():
    """Gets a valid score form the user"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def print_score_status(valid_score):
    """Print what the valid score is worth"""
    if valid_score >= 90:
        print("Excellent")
    elif valid_score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_line_as_stars(valid_score):
    """Prints a number of * equal to the score"""
    print(valid_score * "*")


main()
