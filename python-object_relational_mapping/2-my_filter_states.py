#!/usr/bin/python3
"""obs task-2"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY "
                "'{}' ORDER BY id ASC".format(sys.argv[4]))
    q = cur.fetchall()
    print(row)
    cur.close()
    conn.close()
