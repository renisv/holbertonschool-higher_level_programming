#!/usr/bin/env python3

class CountedIterator:
    """iterator that counts the number of items iterated over."""
    
    def __init__(self, iterable):
        """Initialize the CountedIterator"""
        self.iterator = iter(iterable)
        self.counter = 0
    
    def get_count(self):
        """Return the current count of items iterated over."""
        return self.counter
    
    def __next__(self):
        """Get the next item"""
        item = next(self.iterator)
        self.counter += 1
        return item
    
    def __iter__(self):
        """Return the iterator object itself."""
        return self