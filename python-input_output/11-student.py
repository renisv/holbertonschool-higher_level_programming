#!/usr/bin/python3

"""module about a class"""


class Student:
    """class about a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert to json"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in self.__dict__.keys():
            if key in attrs:
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        """func to replace values"""
        for key in json.keys():
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]
        return self.__dict__
