#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    cmd = "SELECT cities.name FROM cities\
                    JOIN states\
                    ON states.id=cities.state_id\
                    WHERE states.name LIKE BINARY %s\
                    ORDER BY cities.id ASC"
    cursor.execute(cmd, (argv[4], ))
    all_rows = cursor.fetchall()

    print(", ".join([row[0] for row in all_rows]))

    cursor.close()
    conn.close()
