import httpx

url = 'http://www.httpbin.org/headers'
headers = {'User-Agent': 'my-app/0.0.1'}
# 推荐这种语法
with httpx.Client(headers=headers, http2=True) as client:
    response = client.get(url)
    print(response.json()['headers']['User-Agent'])
    