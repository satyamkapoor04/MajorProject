import sqlite3
from sqlite3 import Error

def create_connection (db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print (e)

    return None


def create_table (conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute (create_table_sql)

    except Error as e:
        print (e)


def main():
    database = "/home/satyamk/Documents/majorproject/pythonsqlite.db"
    sql_create_table = """CREATE TABLE IF NOT EXISTS mainproject (keyword04 text PRIMARY KEY, domain04 text, area04 text, keywords04 text, abstract04 text);"""

    conn = create_connection (database)
    if conn is not None:
        create_table (conn,sql_create_table)

    else:
        print ("Error")


if __name__ == '__main__':
    main()
