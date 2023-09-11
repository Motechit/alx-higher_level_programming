#!/usr/bin/python3
"""Defines available attributes/methods of an obj"""


def lookup(obj):
    """Returns the list of available attributes """
    return (dir(obj))
