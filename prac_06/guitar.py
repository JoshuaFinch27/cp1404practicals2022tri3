"""
CP1404Practical - 6
Guitar class
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a programming language instance
        name: str -> reference name for guitar
        year: int -> year that guitar first appeared
        cost: float -> money that the guitar cost
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation in format: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Returns how old the guitar is in years based on current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True if the guitar is >= 50 years old"""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year
