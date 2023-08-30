#!/usr/bin/python3
"""Magic class from the given ByteCode."""
import math


class MagicClass:
    """We iinitialize of the Magic Class"""
    def __init__(self, radius=0):
        """We construct the magic class"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """We calculate the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """We calculate the circumference"""
        return 2 * math.pi * self._MagicClass__radius
