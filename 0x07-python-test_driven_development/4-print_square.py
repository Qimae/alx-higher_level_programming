#!/usr/bin/python3
"""
Module 4-print_square
prints a square with character #
"""


def print_square(size):
    """
    prints a square
    """
    if not isinstance(size, (int, float)) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print("\n".join(["#" * size for i in range(size)]))
