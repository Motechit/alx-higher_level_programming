#!/usr/bin/python3
"""
This is the class Student container
"""


class Student:
    """This is the rep of a student"""
    def __init__(self, first_name, last_name, age):
        """It initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """It returns a dict. rep. of a Student instance"""
        return self.__dict__
