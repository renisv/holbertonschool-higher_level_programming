#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""abstract method introduction"""


class Animal(ABC):
    """define animal"""
    @abstractmethod
    def sound(self):
        """animals make sounds"""
        pass


class Dog(Animal):
    """define dog"""
    def sound(self):
        """dog barks"""
        return ("Bark")


class Cat(Animal):
    """define cat"""
    def sound(self):
        """cat meows"""
        return ("Meow")
