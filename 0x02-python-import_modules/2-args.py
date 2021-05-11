#!/usr/bin/python3
import sys
if __name__ == '__main__':

    largo = len(sys.argv) - 1
    if largo == 0:
        print('{} arguments.'.format(largo))
    else:

        if largo == 1:
            print('{} argument:'.format(largo))
        else:
            print('{} arguments:'.format(largo))

        for i in range(1, largo + 1):
            print('{:d}: {}'.format(i, sys.argv[i]))
