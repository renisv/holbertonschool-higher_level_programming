#!/usr/bin/env python3

if __name__ == "__main__":
    import sys
    
    # Initialize sum to 0
    total = 0
    
    # Iterate through all arguments starting from index 1 (skipping the script name)
    for arg in sys.argv[1:]:
        # Convert each argument to integer and add to total
        total += int(arg)
    
    # Print the result followed by a new line
    print(total)