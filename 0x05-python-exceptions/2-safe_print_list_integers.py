#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0

    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            elements += 1
        except (TypeError, ValueError):
            continue
    print("")
    return elements
