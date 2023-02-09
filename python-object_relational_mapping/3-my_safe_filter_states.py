#!/usr/bin/python3
"""0x0F. Python - ORM - task 2. Filter states by user input"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                "ORDER BY id ASC", (sys.argv[4], ))
    s = cur.fetchall()
    for y in s:
        print(y)
    cur.close()
    conn.close()
