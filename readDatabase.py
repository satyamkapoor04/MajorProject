import sqlite3


connection = sqlite3.connect ("/home/satyamk/Documents/majorproject/pythonsqlite.db")

crsr = connection.cursor()

query = 'SELECT count(keyword04) FROM mainproject'

crsr.execute(query)

ans = crsr.fetchall()

print (ans)
