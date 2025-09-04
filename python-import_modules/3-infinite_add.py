#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nr_of_args = len(argv) - 1

    if nr_of_args == 0:
        print("{}".format(nr_of_args))
    else:
        sum = 0

        for i in range(1, len(argv)):
            sum += int(argv[i])
        print("{}".format(sum))
