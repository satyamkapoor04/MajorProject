import sqlite3
import csv
import ast

connection = sqlite3.connect ("/home/satyamk/Documents/majorproject/pythonsqlite.db")
crsr = connection.cursor()

with open('/home/satyamk/Documents/majorproject/dataset.csv','r') as f:
	read = csv.reader (f)
	i = 0
	for row in read:
		i += 1
		if i != 1:
			data = row[3]
			#print (data)
			data = ast.literal_eval(data)
			size = len(data)
			#print (data)
			for j in range (0,size):
				text = data[j]
				query1 = 'SELECT abstract04 FROM mainproject where keyword04="' + text + '";'
				crsr.execute (query1)
				ans = crsr.fetchall()
				#if (text == "area"):
					#continue
				#print (text)
				L = []
				#print (ans)
				if (len(ans) == 0):
					#print (ans)
					L.append([i-1,j])
					s = "".join(str(L))
					print (s)
					query2 = 'INSERT INTO mainproject (keyword04,abstract04) VALUES("' + text + '","' + s + '");'
					crsr.execute (query2)
				else:
    					crsr.execute (query1)
    					ans = crsr.fetchall()
    					L = ast.literal_eval(ans[0][0])
    					L.append ([i-1,j])
    					s = "".join(str(L))
    					print (s)
    					query3 = 'UPDATE mainproject set abstract04="' + s + '" where keyword04="' + text + '";'
    					crsr.execute (query3)

			connection.commit()
connection.commit()

connection.close()
