#!/usr/bin/python3
"""module for  file reading"""


def read_file(filename=""):
    """reads the file"""
    with open(filename, encoding="UTF8") as file:
        content = file.read()
        print(content, end="")
