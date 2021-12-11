#!/usr/bin/python3
"""
Module 0-add_integer
Defines function add_integer that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Calculates addition

    Attributes:
        a: integer value
        b: integer value
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")   
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
