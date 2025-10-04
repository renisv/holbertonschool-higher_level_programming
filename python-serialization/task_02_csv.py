#!/usr/bin/env python3

import csv
import json
"""reading csv data and convering to json"""


def convert_csv_to_json(csv_file):
    """reading csv data and convering to json"""
    try:
        with open(csv_file, "r") as file:
            csv_dict = csv.DictReader(file)
            json.dump(csv.DictReader(file), file)
            return True
    except FileNotFoundError:
        return False
