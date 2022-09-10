from urllib.parse import urlencode, parse_qs, parse_qsl

params = {
    'name': 'germey',
    'age': 25
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# 反序列化
query = 'name=germey&age=25'
print(parse_qs(query))
# 这个也是反序列化，只不过是用tuple展示
print(parse_qsl(query))