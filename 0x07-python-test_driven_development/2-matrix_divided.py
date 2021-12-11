#!/usr/bin/python3
"""
Module 2-matrix_divided.py
Defines the division of all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Calculates division of all elements

    Attributes:
        matrix: matrix list
        div: division variable
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    newMatrix = []
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        newList = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            newList.append(round(i/div, 2))
            newMatrix.append(newList)
        return newMatrix
