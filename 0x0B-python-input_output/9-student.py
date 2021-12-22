#!/usr/bin/python3
"""
Module 9-student

Defines a class Student with public attribute
first_name, last_name, age
"""


class Student:
    """
    Defines student

    Method:
        __init__(self, first_name, last_name, age)
        to_json(self, attributes=None)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes Student

        Attributes:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """Retrieves dictionary representation"""
        if attributes is None:
            return self.__dict__
        else:
            dic = {}
            for attr in attributes:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic
