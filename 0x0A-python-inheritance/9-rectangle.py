#!/usr/bin/python3
"""
Module 9-rectangle

Defines class Rectangle that inherits from class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
    """
    def __init__(self, width, height):
        """
        Initializes rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints the rectangle description"""
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                self.__width, self.__height))
