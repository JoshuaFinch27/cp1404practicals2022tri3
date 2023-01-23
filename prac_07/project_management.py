"""
2 hours est
actual
+ 20 min
+ 5 min
+ 15 min
"""

import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    """Displays program menu and holds core functions"""
    load(FILENAME)
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass



        elif choice == "R":
            pass
        elif choice == "A":
            pass
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input(">>> ").upper()
    project  .save()
    print("Thank you for using custom-built project management software.")


def display_menu():
    """Display the main menu."""
    print("""
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit""")


def load(self, filename=""):
    """load (from txt file into Project objects in the list)"""
    in_file = open('projects.txt', "r")
    in_file.readline()
    for line in in_file.readlines():
        print(line)
    in_file.close()

main()
