#!/usr/bin/python3
"""
Module 6-peak
Defines find_peak function
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None

    l = list_of_integers
    start = 0
    end = len(l) - 1

    if l[start] > l[start + 1]:
        return l[start]
    if l[end] > l[end - 1]:
        return l[end]

    mid = (start + end)//2
    if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
        return l[mid]
    if l[mid] < l[mid - 1]:
        return find_peak(l[start:mid + 1])
    elif l[mid] < l[mid +1]:
        return find_peak(l[mid:end + 1])
    else:
        return l(start)
