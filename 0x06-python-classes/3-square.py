#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Sqr class body"""

    def __init__(self, size=0):
        """Sqr constructor
        Args:
            size (int): The size of the new sqr
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the new area of the sqr"""
        return (self.__size * self.__size)
