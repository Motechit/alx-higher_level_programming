#!/usr/bin/python3
"""
This python script lists all states from the database hbtn_0e_0_usa with
a given name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", port=3306, user="ubuntu",
                                         passwd="ubuntu", db=argv[3], charset="utf8")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
                            id ASC".format(argv[4]))
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == argv[4]:
                print(row)
        cursor.close()
        db.close()
