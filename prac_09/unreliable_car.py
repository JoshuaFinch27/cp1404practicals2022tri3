"""
CP1404/CP5632 Practical 9
Unreliable Car class
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that is 'unreliable'"""


def __init__(self, name, fuel, reliability):
    """Initialise UnreliableCar class"""
    super().__init__(name, fuel)
    self.reliability = reliability


def drive(self, distance):
    """Drive car based on reliability"""
    if randint(0, 100) >= self.reliability:
        distance = 0
    distance_driven = super().drive(distance)
    return distance_driven
