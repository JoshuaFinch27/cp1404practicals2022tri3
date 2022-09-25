"""
CP1404 - Practical 1
Program that determines score status
"""


def main():
    """Determines score status"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))


def determine_score_status(score):
    """Return what an inputted score is worth"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
