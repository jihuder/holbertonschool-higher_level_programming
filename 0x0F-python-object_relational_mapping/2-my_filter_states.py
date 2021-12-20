#!/usr/bin/python3
'''  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument'''

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    name = argv[4]
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY id ASC""".format(name))

    search = cursor.fetchall()

    for count in search:
        if count[1] == name:
            print(count)

    cursor.close()
    db.close()
