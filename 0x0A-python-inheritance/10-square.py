#!/usr/bin/python3
"""
Module 10-square

Defines class Square that inherits from class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
