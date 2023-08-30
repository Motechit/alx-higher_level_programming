#!/usr/bin/python3
# 2-square.py
"""Square class defination."""


class Square:
    """Sqr class body"""

    def __init__(self, size=0):
        """Sqr class contructor
        Args:
            size (int): This is the size of the new sqr
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
