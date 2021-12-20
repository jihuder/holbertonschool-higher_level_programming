#!/usr/bin/python3
''' the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa '''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    places = cursor.fetchall()
    first = 0
    for count in places:
        if first != 0:
            print(", ", end="")
        print("%s" % count, end="")
        first += 1
    print("")
    cursor.close()
    db.close()
