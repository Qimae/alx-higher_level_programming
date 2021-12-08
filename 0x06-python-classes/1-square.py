#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square defination

    Args:
        size : size of a side of a square
    """
    def __init__(self, size):
        """
        Initalize square

        Attributes:
            size : size of a side of a square
        """
        self.__size = size
