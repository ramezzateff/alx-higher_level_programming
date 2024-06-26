#!/usr/bin/python3
"""Module for add_integers method."""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: the first integer.
        b: the second integer, equal 98.

    Raises:
        TypeError: if a, b not an integer or float.

    Returns:
        The sum of two integers.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
