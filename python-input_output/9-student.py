#!/usr/bin/python3

"""module about a class"""


class Student:
    """class about a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert to json"""
        return self.__dict__
