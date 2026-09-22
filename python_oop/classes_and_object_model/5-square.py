#!/usr/bin/env python3

"""Defines a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a Square with a validated size"""
        self.size = size

    @property
    def size(self):
        """Return the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validating it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
