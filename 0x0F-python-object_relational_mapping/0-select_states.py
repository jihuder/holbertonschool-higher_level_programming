#!/usr/bin/python3
''' list all states from the database hbtn_0e_0_usa'''


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
cr = db.cursor()
cr.execute("SELECT * from states ORDER BY states.id")
states = cr.fetchall()
for state in states:
    print(state)
cr.close()
db.close()
