#!/usr/bin/python3
"""
It contains the load_from_json_file fxn
"""

import json


def load_from_json_file(filename):
    """It creates an Obj from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        create_obj = json.load(file)
        return create_obj
