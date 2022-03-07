#!/usr/bin/python3
"""
Module select_states
Lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main_":
    """Database connection"""
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3])

    """Create cursor to execute queries using SQL"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
