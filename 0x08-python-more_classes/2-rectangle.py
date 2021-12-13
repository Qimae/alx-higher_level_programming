#!/usr/bin/python3
"""
Module 1-rectangle
Defines class Rectangle with private attribute width and height
"""


class Rectangle:
    """
    Defines a rectangle

   Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height]
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        calculates the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
