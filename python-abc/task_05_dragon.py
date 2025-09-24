#!/usr/bin/env python3
"""add functionality to classes in a modular fashion"""


class SwimMixin:
    """Mixin class that provides swimming functionality."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inherits swimming and flying"""

    def roar(self):
        """Print dragon's roar message."""
        print("The dragon roars!")
