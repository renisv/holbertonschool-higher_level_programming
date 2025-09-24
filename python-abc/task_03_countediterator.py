#!/usr/bin/env python3

class CountedIterator:
    """A custom iterator that counts the number of items iterated over."""
    
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        
        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.counter = 0
    
    def get_count(self):
        """
        Return the current count of items iterated over.
        
        Returns:
            int: Number of items iterated so far
        """
        return self.counter
    
    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.
        
        Returns:
            The next item from the iterator
            
        Raises:
            StopIteration: When there are no more items to iterate
        """
        # First try to get the next item
        item = next(self.iterator)
        # If successful, increment counter and return the item
        self.counter += 1
        return item
    
    def __iter__(self):
        """
        Return the iterator object itself.
        
        Returns:
            CountedIterator: The iterator object
        """
        return self