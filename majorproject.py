import sys
import math
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from pandas import read_excel
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import numpy.linalg as LA
import csv
import sqlite3
import ast
import json

#Processing

def elimination (document):
    tokens = nltk.word_tokenize (document)
    data = []
    tagged = nltk.pos_tag (tokens)
    for b in tagged:
        if (not(b[1] == "." or b[1] == "IN" or b[1] == "DT" or b[1] == "PRP$" or b[1] == "(" or b[1] == ")" or b[1] == "," or b[1] == "VBZ" or b[1] == "PRP" or b[1] == "VBD" or b[1] == "CC" or b[1] == "RB" or b[1] == "RBS")):
            data.append (b[0])

    return data


# Send raw query without using set. Gives minimum distance between pair of terms.
def minDist (document,query,maxValue):
    dictionary = []
    len1 = len (document)
    len2 = len (query)
    
    i = 0
    for q in query:
        dictionary.append (q)
        dictionary[i] = []
        i += 1

    for d in range (0,len1):
        for i in range (0,len2):
            if (query[i] == document[d]):
                dictionary[i].append (d)

    sum = 0
    for i in range (0,len2-1):
        for j in range (i+1,len2):
            min = 9999999
            for d1 in dictionary[i]:
                for d2 in dictionary[j]:
                        if ((d2>d1) and min>(d2-d1)):
                            min = (d2-d1)
            if (min != 9999999):
                sum += 1/((2**(j-i-1))*min)

    #Normalising sum
    return sum/maxValue

#same as minDist but for every frequency 
def freqAverageDist (document,query,maxValue):
    dictionary = []
    len1 = len (document)
    len2 = len (query)
    
    i = 0
    for q in query:
        dictionary.append (q)
        dictionary[i] = []
        i += 1

    for d in range (0,len1):
        for i in range (0,len2):
            if (query[i] == document[d]):
                dictionary[i].append (d)

    sum = 0
    pairFreq = 0
    for i in range (0,len2-1):
        for j in range (i+1, len2):
            freq = 0
            count1 = len (dictionary[i])
            count2 = len (dictionary[j])
            l = 0
            m = 0
            result = 0
            while (l<count1 and m<count2):
                if (dictionary[i][l] < dictionary[j][m]):
                    if (l == count1-1 or dictionary[i][l+1]>dictionary[j][m]):
                        result += (dictionary[j][m]-dictionary[i][l])
                        l += 1
                        m += 1
                        freq += 1
                        if (freq == 1):
                            pairFreq += 1
                    else:
                         l += 1
                else:
                     break

            if (result != 0):
                sum += (freq)/((2**(j-i-1))*result)

    #Normalising sum
    return (2*sum)/((maxValue*(len2)*(len2-1))+1)


#for minDist
def findingMaxValue (size):
    sum = 0
    i = 0
    for j in range (size-1,0,-1):
        sum += j/(2**i)
        i += 1


    return math.ceil(sum+1)

#(frequency/difference in distance)

def avg_dist (document,query):
    dictionary = {}
    for q in query:
        dictionary[q] = []

    len1 = len(document)
    len2 = len(query)

    x = 0 #number of queries found

    for i in range(0,len1):
        if document[i] in dictionary:
            dictionary[document[i]].append (i)

    ll = []

    for key in list(dictionary):
        if (not dictionary[key]) :
            del dictionary[key]
        else:
            x += 1
            ll.append(dictionary[key])

    if (x == 0):
        return 0

    result = 0
    llLen1 = len(ll)
    for i in range(0,llLen1-1):
        for j in range(i+1,llLen1):
            sum = 0
            for k in ll[i]:
                for l in ll[j]:
                    sum += abs(k-l)
            result += (len(ll[i])*len(ll[j]))/sum


    a = (x-1)/len2
    b = (x)/len2

    res = (b-a)*result
    lenn = (len2*(len2-1))/2
    res = (res/(lenn+1))+a

    return res

#minimum segment of document

def minCoverage (document,qy):
    hash_ptr = {}
    hash_str = {}
    len1 = len(document)
    query_len = len(qy)
    
    query = []
    for i in range (0,len1):
        if ((document[i] in qy) and not(document[i] in query)):
            query.append(document[i])

    len2 = len(query)
    diff = (len1-len2)
    if (len2 == 0):
        return 0

    for q in query:
        hash_ptr[q] = 1
        hash_str[q] = 0
    start = 0
    min_len = 99999999
    count = 0
    for j in range (0,len1):
        if document[j] in hash_ptr:
            if (hash_str[document[j]] == 0):
                count += 1
            hash_str[document[j]] += 1
        if count == len2:
            while (not(document[start] in hash_ptr) or hash_str[document[start]] > 1):
                if (document[start] in hash_ptr):
                    hash_str[document[start]] -= 1
                start += 1

            len_window = j-start+1
            if (min_len > len_window):
                min_len = len_window

    return ((len2/min_len)*(1/(diff+1)))



def tfidfcosine (train_set,test_set):
	#stopWords = stopwords.words('english')
	vectorizer = CountVectorizer()
	#print (vectorizer)
	transformer = TfidfTransformer()
	#print transformer
	#
	#
	score = []
	score2 = []
	size = len (train_set)

	for i in range (0,size):
    		score2.append(0)

    		
	try:
		trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
		testVectorizerArray = vectorizer.transform(test_set).toarray()
	except:
    		#print ("Error Raised")
    		return score2

	#print ('Fit Vectorizer to train set', trainVectorizerArray)
	#print ('Transform Vectorizer to test set', testVectorizerArray)
	np.seterr (divide='ignore',invalid='ignore')
	cx = lambda a, b : round(np.inner(a, b)/(LA.norm(a)*LA.norm(b)), 3)
	
	for vector in trainVectorizerArray:
    		#print (vector)
		for testV in testVectorizerArray:
        		#print (testV)
        		cosine = cx(vector, testV)
        		score.append(cosine)

	transformer.fit(trainVectorizerArray)
	#print
	#print (transformer.transform(trainVectorizerArray).toarray())

	transformer.fit(testVectorizerArray)
	#print 
	tfidf = transformer.transform(testVectorizerArray)
	#print (tfidf.todense())
	return score



def retrieve (query):
    connection = sqlite3.connect ("pythonsqlite.db")
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
    with open('dataset.csv','r') as f:
        read = csv.reader (f)
        excel = read_excel ("Data.xlsx")
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

    return output




def mainFunction(q):
    #document = read_excel ("Data1.xlsx")
    #domain = document.Domain
    #area = document.area
    #keywords = document.keywords
    #abstract = document.Abstract
    #size = len (domain)
    #print (abstract)
    data1 = []
    data2 = []
    query = elimination(q)
    data = retrieve (query)
    data1.append(" ".join(query))
    for d in data:
        str1 = " ".join(d[3])
        data2.append(str1)

    #print (data2)
    #print (data2)
    tfidfScore = tfidfcosine (data2,data1)

    set_of_query_terms = set(query)

    minCoverageValues = []
    avgDistValues = []
    minDistValues = []
    freqAverageDistValues = []
    maxValueForMinDist = findingMaxValue (len(query))



    i = 0
    for d in data:
        #print (d)
        d.append (minDist(d[3],query,maxValueForMinDist))
        d.append (freqAverageDist(d[3],query,maxValueForMinDist))
        d.append (minCoverage(d[3],set_of_query_terms))
        d.append (avg_dist(d[3],set_of_query_terms))
        d.append (tfidfScore[i])
        i += 1

    for d in data:
        d.append (0.05*d[7]+0.95*d[8]+0.95*d[9]+0.2*d[10]+0.2*d[11])

    #for i in range (0,size):
        #result.append([domain[i],area[i],keywords[i],abstract[i],(1.0*freqAverageDistValues[i])+(0.0*minDistValues[i])+(0.0*tfidfScore[i])+(0.0*minCoverageValues[i])+(0.0*avgDistValues[i])])

    data.sort (reverse=True, key=lambda x: x[12])

    res_len = len(data)

    return data

def retrieveRelatedDocuments (q,k):
    query = []
    for qq in q:
        qqq = nltk.word_tokenize (qq)
        for qqqq in qqq:
            query.append (qqqq)
            
    connection = sqlite3.connect ("pythonsqlite.db")
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
    excel = read_excel ("Data.xlsx")
    abstract = excel.Abstract
    i = 1
    j = 0
    size = len(document)
    ab = len (abstract)
    for i in range(0,ab):
        if (j < 10):
            if (document[j]-1 == i):
                output.append (abstract[i])
                j = j+1
                
    name = "../images/file" + str(k) + ".txt"
    json_string = json.dumps(output)
    f = open (name,"w")
    f.write (json_string)
    f.close()
