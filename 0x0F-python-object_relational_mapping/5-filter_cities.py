#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state"""
import MySQLdb as sql
from sys import argv


if __name__ == '__main__':
        conn = sql.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.name FROM states INNER JOIN cities " +
                    "ON cities.state_id = (SELECT id FROM states WHERE "
                    "name = '{}') GROUP BY cities.id;". format(argv[4], ))
        query_rows = cur.fetchall()
        auxlist = ()
        for row in query_rows:
                auxlist += row
        print(", ".join(auxlist))
        cur.close()
        conn.close()
