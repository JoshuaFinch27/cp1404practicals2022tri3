"""
CP1404 Practical - 7
Program:
- reads guitars.csv
- stores info as Guitar objects
- display with loop
- THEN sort by year (oldest to newest) & display again
"""

from prac_06.guitar import Guitar


def main():
    """Guitar file reader using the csv module."""
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    # File format is like: Name,Year,Cost
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
    in_file.close()
    for guitar in guitars:
        print(guitar)
    sort_guitars(guitars)


def sort_guitars(guitars):
    """Sort guitars by oldest to newest"""
    iteration = 1
    for guitar in guitars:
        if guitar.__lt__(guitars):
            guitar.pop()
            guitar.append(guitars[iteration])
        iteration += 1
    for guitar in guitars:
        print(guitar)
        # Couldn't get this, moving on


main()
