from requests import Request, Session

url = 'https://www.httpbin.org/post'

data = {
    'name': 'germey',
    'age': 25
}

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/ 537.36'
}

s = Session()
# 构造Request对象
req = Request('POST', url, data=data, headers=headers)
# 必须调用session的prepare方法，变成prepared request(转换类型)
prepared = s.prepare_request(req)

r = s.send(prepared)

print(r.text)