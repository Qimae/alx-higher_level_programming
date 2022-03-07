#!/usr/bin/python3
"""
Module select_states
Lists all states with a name starting with N from the database
"""


import MySQLdb
from sys import argv

if __name__ == "__main_":
    """Database connection"""
    conn = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states where name LIKE BINARY 'N%' ORDERBY id ASC")
    for i in cursor.fetchall():
        print(i)
