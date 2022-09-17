import json

with open('data.json', 'r') as f:
    str = f.read()
    print(type(str))
    # 还可以简写(注意不是loads)
    # data = json.load(open('data.json', 'r', encoding='utf-8'))
    data = json.loads(str)
    print(data)
    print(type(data))

    print(data[0]['name'])
    # get方式获得的value，如果key不存在，返回None
    print(data[0].get('name'))
    # getOrDefault
    print(data[0].get('age', 25))


# 输出json
data = [
    {
        'name': '冀宁',
        'gender': 'Male',
        'birthday': '1992-10-18'
    }
]
# 也可以这样简写
# json.dump(data, open('output.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
with open('output.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=4, ensure_ascii=False))