#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML to dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
