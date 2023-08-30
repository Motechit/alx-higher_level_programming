#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): The size of the new sqr
        """
        self.size = size

    @property
    def size(self):
        """Returns new size of the sqr"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the sqr"""
        return (self.__size * self.__size)
