# -*- coding: utf-8 -*-

from urllib import request
import json
import csv
from pymongo import MongoClient
host = "127.0.0.1"
port = 27017

client = MongoClient(host, port)
db = client['jc']

url = 'http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=had'
req = request.Request(url='%s' % url)
res = request.urlopen(req)
res = res.read()
resp = res.decode('raw_unicode_escape').split('(')[1].split(')')[0]
# print(res.decode('unicode_escape'))
# 输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'


resp = res.decode(encoding='utf-8').split('(')[1].split(')')[0]
params = json.loads(resp)
data = params['data']
d = {}

csvfile = open('test.csv','w', newline='')
writer = csv.writer(csvfile)
writer.writerow(['num', 'h', 'd', 'a'])
for key in data.keys():
    csv = []
    d['id'] = data[key]['id']
    d['a'] = float(data[key]['had']['a'])
    d['d'] = float(data[key]['had']['d'])
    d['h'] = float(data[key]['had']['h'])
    d['num'] = data[key]['num']
    d['h_cn'] = data[key]['h_cn']
    d['h_id'] = data[key]['h_id']
    d['a_cn'] = data[key]['a_cn']
    d['a_id'] = data[key]['a_id']
    d['date'] = data[key]['date']
    d['time'] = data[key]['time']
    print(d)
    #db.match.insert(d)
    csv.append(d['num'])
    csv.append(d['h'])
    csv.append(d['d'])
    csv.append(d['a'])
    writer.writerow(csv)
csvfile.close()
# resp = res.decode(encoding='utf-8').split('(')[1].split(')')[0]
# params = json.loads(resp)
# print(resp)
