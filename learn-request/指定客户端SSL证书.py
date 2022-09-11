import requests

# 文件路径随便给的，需要真的有这两个文件
r = requests.get('https://ssr2.scrape.center', cert=('/path/server.crt', '/path/server.key'))
print(r.status_code)