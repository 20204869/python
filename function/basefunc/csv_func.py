# -*- coding: utf-8 -*-

'''
csv文件数据处理
'''

import csv

#不同方式读取csv文件
with open('../data/data-text.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #for row in spamreader:
        #print(row)


csvfile_1 = open('../data/data-text.csv')
print(type(csvfile_1))  # 返回<class '_io.TextIOWrapper'> 返回一个文件对象
reader = csv.DictReader(csvfile_1)
#for row in reader:
    #print (row)

csvfile_2 = open('../data/data-text.csv')
reader = csv.reader(csvfile_2)
#for row in reader:
    #print (row)

