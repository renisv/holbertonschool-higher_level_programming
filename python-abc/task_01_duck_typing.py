#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math
"""abstract method introduction"""


class Shape(ABC):
    """abstract class for shapes"""
    def area(self):
        """defines area"""
        pass

    def perimeter(self):
        """deifnes perimeter"""
        pass


class Circle(Shape):
    """"defines circle shape"""
    def __init__(self, radius):
        """initializes a circle"""
        self.radius = radius

    def area(self):
        """"defines circle area"""
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """defines circle perimeter"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """defines rectangle shape"""
    def __init__(self, width, height):
        """"initializes a rectanlge"""
        self.width = width
        self.height = height

    def area(self):
        """defines rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """defines rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape_example):
    """gives shape info"""
    print(f"Area: {shape_example.area()}")
    print(f"Perimeter: {shape_example.perimeter()}")
