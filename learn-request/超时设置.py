import requests

# 可以直接给数字，比如timeout=5，代表连接+读取的总超时时间
# 也可以给元组，第一个参数代表连接时间，第二个参数代表读取时间
r = requests.get('https://www.httpbin.org/get', timeout=(5, 30))

print(r.status_code)