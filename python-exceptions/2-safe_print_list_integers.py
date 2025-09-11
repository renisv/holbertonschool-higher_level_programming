#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            print("{:d}".format(my_list[x]))
            count +=1
            return count
    except (ValueError, IndexError):
        return count
