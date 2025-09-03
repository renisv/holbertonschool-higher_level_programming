def islower(c):
    """Check if a character is lowercase."""
    # Get the ASCII value of the character
    ascii_value = ord(c)
    
    # Check if it's in the lowercase range (97 to 122)
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False