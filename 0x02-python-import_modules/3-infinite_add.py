#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    size = len(sys.argv)
    if (size > 1):
        for j in range(1, size):
            result += (int(sys.argv[j]))
    print('{:d}'.format(result))
