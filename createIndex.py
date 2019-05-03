import csv
import sqlite3

with open('/home/satyamk/Documents/majorproject/dataset1.csv','rb') as f:
    reader = csv.DictReader(f)
    print (reader[1])
