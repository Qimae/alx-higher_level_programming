#!/usr/bin/python3
"""
Module 5-text_indentation
prints a text with 2 new lines after . ? : characters
"""


def text_indentation(text):
    """
    prints a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines_list = [lines.strip(' ') for lines in text.split('\n')]
    new = "\n".join(lines_list)
    print(new, end="")
