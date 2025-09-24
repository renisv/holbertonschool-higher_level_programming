#!/usr/bin/env python3
"""extend built-in classes to add or modify behavior"""


class VerboseList(list):
    """class that extends list"""
    def append(self, item):
        """overwriting append"""
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, my_list):
        """overwriting extend"""
        count = len(my_list)
        super().extend(my_list)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """overwriting remove"""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """"overwriting pop"""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
