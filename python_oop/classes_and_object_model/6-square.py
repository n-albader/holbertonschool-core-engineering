#!/usr/bin/env python3

"""Defines a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a validated size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the current square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position after validating it"""
        if not isinstance(value, tuple):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        if len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        if not isinstance(value[0], int):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        if not isinstance(value[1], int):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        if value[0] < 0 or value[1] < 0:
           raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the square representation"""
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]

        for row in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size

            if row < self.__size - 1:
                result += "\n"

        return result
