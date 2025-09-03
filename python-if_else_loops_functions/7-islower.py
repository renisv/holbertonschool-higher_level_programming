#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase."""
    ascii_value = ord(c)

    if 97 <= ascii_value <= 122:
        return True
    else:
        return False
