#!/usr/bin/python3
"""Module about a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that implements a square"""
    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Func to calculate area"""
        return self.__size ** 2
