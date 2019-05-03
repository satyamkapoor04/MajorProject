import sqlite3
import ast
import csv
from pandas import read_excel

def retrieve (query):
    connection = sqlite3.connect ("/home/satyamk/Documents/majorproject/pythonsqlite.db")
    crsr = connection.cursor()
    document = set()
    for q in query:
        pas = 'SELECT abstract04 FROM mainproject where keyword04="' + q + '";'
        crsr.execute (pas)
        ans = crsr.fetchall()
        if (len(ans) != 0):
            data  = ast.literal_eval (ans[0][0])
            for d in data:
                document.add (d[0])

    document = list(document)
    document.sort()
    
    output = []
    #print (document)
    with open('/home/satyamk/Documents/majorproject/dataset.csv','r') as f:
        read = csv.reader (f)
        excel = read_excel ("/home/satyamk/Desktop/Dataset/Meta-data/Data.xlsx")
        domain = excel.Domain
        area = excel.area
        keywords = excel.keywords
        abstract = excel.Abstract
        i = 0
        j = 0
        size = len(document)
        for row in read:
            if (i != 0):
                if (j<size and document[j]-1 == i):
                    output.append ([row[0],row[1],row[2],ast.literal_eval(row[3]),area[i-1],keywords[i-1],abstract[i-1]])
                    j += 1
            i += 1

    for o in output:
        print (o[3])

retrieve (["machine","learning"])
