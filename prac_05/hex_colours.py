"""
CP1404 - Practical 5
Program that: Allows the user to look up  hexadecimal colour codes
"""

HEX_COLOUR_CODES = {"Absolute Zero": "#0048ba", "Alizarin crimson": "#e32636",
                    "Amaranth": "#e52b50", "Amber": "#ffbf00",
                    "Amethyst": "#9966cc", "Aqua": "#00ffff",
                    "Aureolin": "#fdee00", "Barn Red": "#7c0a02",
                    "Battleship Gray": "#848482", "Blue Green": "#0d98ba"}
print(HEX_COLOUR_CODES)
colour_name = input("Enter the name of a colour: ")
while colour_name != "":
    print(f"The code for {colour_name} is {HEX_COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
print("Thanks for looking up colour codes!")
