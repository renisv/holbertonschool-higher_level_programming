#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nr_of_args = len(argv) - 1

    if nr_of_args == 1:
        print("{} argument:".format(nr_of_args))
    elif nr_of_args > 1:
        print("{} arguments:".format(nr_of_args))
    else:
        print("{} arguments.".format(nr_of_args))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
