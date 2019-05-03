import csv

with open('dataset.csv','r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        print (row[3])
        print ("----")

readFile.close()
