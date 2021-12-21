#!/usr/bin/python3
"""
Module 1-my_list
defines class MyList that inherits from class list
"""


class MyList(list):
    """
    inherits from list

    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """
        prints sorted list (ascending)
        """
        print(sorted(self))
