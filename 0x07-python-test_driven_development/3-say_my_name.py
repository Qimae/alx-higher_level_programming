#!/usr/bin/python3
"""
Module 3-say_my_name
Defines function say_my_name and prints My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """
    Prints the first name and last name

    Attributes:
        first-name: String first name
        last_name: String last name
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
