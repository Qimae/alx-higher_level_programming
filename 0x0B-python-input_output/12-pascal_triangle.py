#!/usr/bin/python3
"""
Module 12-pascals_triangle

Defines a function that returns a list if integers
representing the pascal's triangle of n
"""


def pascal_triangle(n):

    """returns a list of integers in pascals triangle"""
    if n <= 0:
        return []
    if n  == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
