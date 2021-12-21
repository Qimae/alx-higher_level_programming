#!/usr/bin/python3
"""
Module 7-base_geometry

Defines class BaseGeometry
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validates value

        Attributes:
            name: string
            value: element to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
           raise ValueError("{:s} must be greater than 0".format(name))
