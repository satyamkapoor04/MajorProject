import csv
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

#Processing

def elimination (document):
    tokens = nltk.word_tokenize (document)
    data = []
    tagged = nltk.pos_tag (tokens)
    for b in tagged:
        if (not(b[1] == "." or b[1] == "IN" or b[1] == "DT" or b[1] == "PRP$" or b[1] == "(" or b[1] == ")" or b[1] == "," or b[1] == "VBZ" or b[1] == "PRP" or b[1] == "VBD" or b[1] == "CC" or b[1] == "RB" or b[1] == "RBS")):
            data.append (b[0])

    return data

fields = ['Domain','Area','Keywords','Abstract']
rows = [[]]
document = read_excel ("/home/satyamk/Desktop/Dataset/Meta-data/Data.xlsx")
domain = document.Domain
area = document.area
keywords = document.keywords
abstract = document.Abstract

size = len(domain)

writer = 0

with open('dataset.csv','a') as writeFile:
    writer = csv.writer (writeFile)
    writer.writerow(fields)
    for i in range (0,size):
        writer.writerows([[domain[i],area[i],keywords[i],elimination(abstract[i])]])

writeFile.close()

