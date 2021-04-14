# -*- coding: utf-8 -*-

'''
json文件数据处理
loads()：将json数据转化成dict数据  PS：接受字符串作为参数
dumps()：将dict数据转化成json数据
load()：读取json文件数据，转成dict数据
dump()：将dict数据转化成json数据后写入json文件
'''
import json

#read json file and print
json_data = open('../data/data-text.json').read()
print((type(json_data)))  #返回 <class 'str'>
data = json.loads(json_data)
#for item in data:
    #print (item)

with open('../data/data-text.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    print('这是文件中的json数据：',json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))


dict1 = {'name': '张三', 'age': 18, 'sex': '男'}
dict2='{"name": "张三", "age": 18, "sex": "男"}'
#json to dict
print('这是转换后的数据：',json.loads(dict2))
print('这是转换后的数据类型：',type(json.loads(dict2)))

#dict to json
print('这是将字典转换之后的数据：',json.dumps(dict1,ensure_ascii=False))
print('这是将字典转换之后的数据类型：',type(json.dumps(dict1,ensure_ascii=False)))

#data write json file
with open('../data/write_json.json', 'a', encoding='utf8')as fp:
    json.dump(dict1,fp,ensure_ascii=False)
