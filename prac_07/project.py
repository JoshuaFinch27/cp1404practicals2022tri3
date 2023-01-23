"""
Prac 7 - Project Class
"""

import datetime


class Project:
    """Creates Project objects, and holds methods relating to them"""

    def __init__(self, name="", start_date=00/00/0000, cost_estimate=0, completion_percentage=0):
        """Initialise a place"""
        self.name = name
        self.start_date = start_date
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


