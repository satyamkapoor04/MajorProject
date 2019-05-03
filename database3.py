import sqlite3

connection = sqlite3.connect ("/home/satyamk/Documents/majorproject/pythonsqlite.db")

crsr = connection.cursor()

sql_command = """DELETE FROM mainproject"""

try:
    crsr.execute(sql_command)
    print ("First Successful")
    try:
        crsr.execute(sql_command)
        print ("Second Successful")

    except:
        print ("Second Fail")


except:
    print ("First Fail")

connection.commit()
connection.close()
