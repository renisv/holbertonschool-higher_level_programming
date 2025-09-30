#!/usr/bin/python3

"""module to manipulate file"""

import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list1 = []
if os.path.exists("add_item.json"):
    list1 = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    list1.append(argv[i])
save_to_json_file(list1, "add_item.json")
