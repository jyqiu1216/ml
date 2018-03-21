# -*- coding: utf-8 -*-
import csv
from sklearn import tree
from pymongo import MongoClient
host = "127.0.0.1"
port = 27017

client = MongoClient(host, port)
db = client['jc']

odds_list = []
lable = []

matchs = db.all_match.find()

# read csv file
csvfile = open('test.csv', 'r')
reader = csv.reader(csvfile)
data = []
testdata = []
for item in reader:
    tmp = []
    if item[0] == 'num':
        continue
    data.append(item)
    tmp.append(float(item[1]))
    tmp.append(float(item[2]))
    tmp.append(float(item[3]))
    testdata.append(tmp)
print(testdata)

for match in matchs:
    odds = []
    h_odds = match['h_odds']
    d_odds = match['d_odds']
    a_odds = match['a_odds']
    if h_odds == '--' or d_odds == '--' or a_odds == '--':
        continue
    odds.append(float(h_odds))
    odds.append(float(d_odds))
    odds.append(float(a_odds))
    odds_list.append(odds)
    lable.append(float(match['result']))

# feature = [[178, 1], [155, 0], [177, 0], [165, 0], [169, 1], [160, 0]]

# lable = ['male', 'female', 'male', 'female', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(odds_list, lable)

result = clf.predict(testdata)

for i in range(0, len(data)):
    data[i].append(result[i])
print(data)
