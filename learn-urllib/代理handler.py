from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})

opener = build_opener(proxy_handler)

try:
    result = opener.open('http://www.baidu.com')
    print(result.read().decode('utf-8'))
except URLError as e:
    print(e.reason)