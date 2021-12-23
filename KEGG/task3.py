from sklearn import linear_model
import pandas
import numpy
import matplotlib
import matplotlib.pyplot as plt
import csv
import time
import json
from Bio.KEGG import REST

f = open('/Users/youngkim/Desktop/Research/Biopython_research/Pyruvate_Kinase.txt', 'r')

listset = []
`
while True:
    line = f.readline()
    temp = ' '.join(line.split('    ')).split(":")
    listset.append(temp)
    if not line:
        break

f.close()
exlist = listset[1:]
print(exlist[0:4])
classnames = ['NAME', 'CLASS', 'SYSNAME', 'REACTION', 'ALL_REAC', 'SUBSTRATE', 'PRODUCT', 'COMMENT', 'HISTORY', 'REFERENCE', 'PATHWAY', 'ORTHONOLOGY', 'GENES']
myDict = {}
flag = 0
sum = 0

for a in range (5):
    start = time.time()
    for i in range (0, len(exlist)):
        for c in classnames:
            if c in exlist[i][0]:
                print(exlist[i][0])
                temp = []
                flag = 1
                exlist[i][0] = exlist[i][0].replace(c, '')
                print(exlist[i])
                while exlist[i][0][-2] == ';':
                    temp.appen(exlist[i][0])
                    if i<len(exlist):
                        i = i+1
                temp.appen(exlist[i][0])
                print(exlist[i][0])
                myDict[c] = temp

    end = time.time()
    sum = sum + end - start

print (sum/5)
print ("dict\n ", myDict)