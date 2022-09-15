"""
CP1404 - Practical 1
Menu using the standard while loop pattern
"""

MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU_STRING)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU_STRING)
    menu_choice = input(">>> ").upper()
print("Finished.")
