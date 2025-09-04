#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    for arguments in range(1,len(sys.argv)):
        print("{}: {}".format(arguments, sys.argv[arguments]))
