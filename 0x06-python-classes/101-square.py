#!/usr/bin/python3
"""Sqr class defination."""


class Square:
    """Sqr class body"""

    def __init__(self, size=0, position=(0, 0)):
        """Sqr constructor
        Args:
            size (int): The size of the new sqr
            position (int, int): The position of the new sqr
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """The getter and setter to the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The getter and setter to the current position of the sqr"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """It returns the current area of the sqr"""
        return (self.__size * self.__size)

    def my_print(self):
        """It prints the sqr with the # char"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """We define the print() rep. of a Sqr"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
