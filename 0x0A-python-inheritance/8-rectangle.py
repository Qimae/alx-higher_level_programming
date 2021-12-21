#!/usr/bin/python3
"""
Module 8-rectangle

Defines class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """
        Initializes rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
