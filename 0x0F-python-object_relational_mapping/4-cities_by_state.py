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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    places = cursor.fetchall()
    for count in places:
        print(count)
    cursor.close()
    db.close()
