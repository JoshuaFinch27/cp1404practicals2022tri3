"""
CP1404 - Practical 5
Program that: states names that are in a dictionary
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except ValueError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_abbreviation, state_name in CODE_TO_NAME.items():
    print(f"{state_abbreviation:3s} is {state_name}")
