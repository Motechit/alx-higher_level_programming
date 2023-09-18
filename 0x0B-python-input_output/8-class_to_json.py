#!/usr/bin/python3
"""
The "class_to_json" function container
"""


def class_to_json(obj):
    """It returns the dict. description with simple data structure
    for JSON serialization of an object"""
    return obj.__dict__
