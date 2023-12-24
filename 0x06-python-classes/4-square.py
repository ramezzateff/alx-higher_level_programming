#!/usr/bin/pytho3
"""Deine a class Square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size(int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.size = size * size
