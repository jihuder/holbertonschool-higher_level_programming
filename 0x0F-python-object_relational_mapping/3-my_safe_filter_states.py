#!/usr/bin/python3
'''  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states\
                WHERE name LIKE %s\
                ORDER BY states.id", (argv[4],))
    search = cursor.fetchall()
    for count in search:
        print(count)
    cursor.close()
    db.close()
