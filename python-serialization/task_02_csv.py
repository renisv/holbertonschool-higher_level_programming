#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_file):
    """reading csv data and converting to json"""
    try:
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
