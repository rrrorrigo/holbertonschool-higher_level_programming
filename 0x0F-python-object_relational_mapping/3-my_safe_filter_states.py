#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table. And safe from SQL Injections"""
import MySQLdb as sql
from sys import argv


if __name__ == '__main__':
        conn = sql.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cmd = "SELECT * FROM states WHERE name=%s"
        cur.execute(cmd, (argv[4],))
        query_rows = cur.fetchall()
        for row in query_rows:
                print(row)
        cur.close()
        conn.close()
