"""
CP1404 - Practical 4
Program that: asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Each line should be in the shown formatting
"""

import random

NUMBERS_GENERATED_FOR_LINE = 6
MINIMUM_POSSIBLE = 1
MAXIMUM_POSSIBLE = 45


def main():
    """Picks sets of 6 random numbers * user input"""
    generated_picks = int(input("How many quick picks? "))
    while generated_picks <= 0:
        print("You must enter a number greater than or equal to 0")
        generated_picks = int(input("How many quick picks? "))
    for pick in range(generated_picks):
        quick_pick = []
        for i in range(NUMBERS_GENERATED_FOR_LINE):
            number = random.randint(MINIMUM_POSSIBLE, MAXIMUM_POSSIBLE)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
