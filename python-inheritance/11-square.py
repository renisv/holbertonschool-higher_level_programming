#!/usr/bin/python3

"""Module about a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class implements a square"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Func to calculate area"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
