"""
Prac 7 - Project Class
"""

import datetime


class Project:
    """Creates Project objects, and holds methods relating to them"""

    def __init__(self, name="", start_date=00 / 00 / 0000, priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a place"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Returns a string with details about a project"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def update_priority(self, percentage):
        """Changes percentage_completed of selected project"""
        self.completion_percentage = percentage
