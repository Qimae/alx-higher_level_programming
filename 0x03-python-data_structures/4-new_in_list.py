#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listCopy = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        listCopy[idx] = element
        return listCopy
