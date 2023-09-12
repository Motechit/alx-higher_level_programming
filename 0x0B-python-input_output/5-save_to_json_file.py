#!/usr/bin/python3
"""
This is the "save_to_json_file" fxn container
"""

import json


def save_to_json_file(my_obj, filename):
    """It writes an Obj to a txt file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
