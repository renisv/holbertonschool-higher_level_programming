#!/usr/bin/python3
""" This creates a class square with private attribute size """


class Square:
    """  This creates a class square with private attribute size """
    def __init__(self, size=0):
        """ Initializes a square with default size 0 """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """get the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """give value to size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """"Calculate and return the area of the square"""
        return self.__size * self.__size
