#!/usr/bin/python3
"""It defines class BaseGeometry"""


class BaseGeometry:
    """Body of the class"""

    def area(self):
        """Not to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter format
            TypeError: value is not an int
            ValueError: value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
