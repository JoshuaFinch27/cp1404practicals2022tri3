"""
CP1404 Practical - 6: Simple class for programming languages

Start: 10:17am
Finish:
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance
        name: str -> reference name for language
        typing: str -> static or dynamic
        reflection: bool: is reflection? yes/no
        year: int -> year that language first appeared
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True/False if the language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string representation in format: Python, Dynamic Typing, Reflection=True, First appeared in 1991"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
