#!/usr/bin/python3
"""this module defines a rectangle"""


class Rectangle:
    """this class defines a rectangle"""
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """get current width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """give value to width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """get current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """give value to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
