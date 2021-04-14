import json

if __name__ == '__main__':
    dict='{"name": "张三", "age": 18, "sex": "男"}'
    print(type(dict))
    print(json.loads(dict))