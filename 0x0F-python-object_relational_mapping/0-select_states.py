#!/usr/bin/python3
"""
This python script lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="ubuntu", passwd="ubuntu", db="hbtn_0e_0_usa")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row) 
    cursor.close()
    db.close()
