#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    input = argv[1:]
    size = len(input)

    if(size == 1):
        print('{} argument:'.format(size))
    elif(size > 1):
        print('{} arguments:'.format(size))
    else:
        print('{} arguments.'.format(size))
    i = 1
    for i, arg in enumerate(input):
        print('{:d}: {:s}'.format(i + 1, arg))
