#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table"""
import MySQLdb as sql
from sys import argv


if __name__ == '__main__':
        conn = sql.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM states WHERE name = '{}'"
                    .format(argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
                print(row)
        cur.close()
        conn.close()
