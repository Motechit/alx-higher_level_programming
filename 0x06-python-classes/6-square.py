#!/usr/bin/python3
"""Sqr class definatn"""


class Square:
    """Sqr class body"""

    def __init__(self, size=0, position=(0, 0)):
        """Sqr constructor
        Args:
            size (int): The size of the new sqr
            sqr position (int, int): of Tupple
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is the getter and getter of a sqr"""
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
        """This is the getter and Setter for position of the sqr"""
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
        """It returns new area of the sqr"""
        return (self.__size * self.__size)

    def my_print(self):
        """It prints the stdout to the sqr with the char"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
