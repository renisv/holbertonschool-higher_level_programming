#!/usr/bin/env python3
""" extends the built-in iterator"""


class CountedIterator:
    """A custom iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """constructs the class"""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """counts"""
        return self.counter

    def __next__(self):
        """Increment counter and get next item in one line"""
        self.counter += 1
        return next(self.iterator)

    def __iter__(self):
        """returns self"""
        return self
