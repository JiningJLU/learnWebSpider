import requests

proxies = {
    'http': 'http://10.10.10.10:1080',
    'https': 'http://10.10.10.10:1080',
}

# 如果代理需要身份认证
# proxies = {'https': 'http://user:password@10.10.10.10:1080'}

requests.get('https://www.httpbin.org/get', proxies=proxies)