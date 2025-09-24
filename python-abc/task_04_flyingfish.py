#!/usr/bin/env python3
"""inherit attributes and behaviors from more than one parent"""


class Fish:
    """Fish class representing aquatic animals."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """Bird class representing flying animals."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        """Override fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method"""
        print("The flying fish lives both in water and the sky!")
