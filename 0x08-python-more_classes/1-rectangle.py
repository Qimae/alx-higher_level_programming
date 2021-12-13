#!/usr/bin/python3
"""
Module 1-rectangle
Defines class Rectangle with private attribute width and height
"""


class Rectangle():
    """
    Defines a rectangle

    Attributes:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height]
        """
        self.width = width
        self.height = height

    def width(self):
        """
        retrieves the width of a rectangle
        """
        return self.__width

    def width(self, value):
        """
        sets the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    def height(self):
        """
        retrieves the height of a rectangle
        """
        return self.__height
    
    def height(self, value):
        """
        sets the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
