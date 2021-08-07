#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb as sql
from sys import argv


if __name__ == '__main__':
        conn = sql.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM states " +
                    "INNER JOIN cities ON states.id = cities.state_id;")
        query_rows = cur.fetchall()
        for row in query_rows:
                print(row)
        cur.close()
        conn.close()
