#!/usr/bin/env python3

import pickle
"""module that serializes and deserializes with pickle"""


class CustomObject:
    """object made for testing pickle implementation"""
    def __init__(self, name, age, is_student):
        """initializing custom object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displaying object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """pickle serialization"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """pickle deserialization"""
        try:
            with open(filename, "rb") as file:
                python_object = pickle.load(file)
                return python_object
        except FileNotFoundError:
            return None
