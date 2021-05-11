#!/usr/bin/python3
import sys
if __name__ == '__main__':

    largo = len(sys.argv)

    adicion = 0
    for i in range(1, largo):
        adicion += int(sys.argv[i])
    print(adicion)
