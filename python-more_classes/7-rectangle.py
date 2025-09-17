#!/usr/bin/python3
"""this module defines a rectangle"""


class Rectangle:
    """this class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """define the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """define the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """"prints the rectangle with #"""
        new_string = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                new_string += str(self.print_symbol)
            if i != self.height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """string represantation of a rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """instance of deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
