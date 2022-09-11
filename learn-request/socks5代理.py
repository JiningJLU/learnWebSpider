# pip3 install "requests[socks]"

import requests

proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}


requests.get('https://www.httpbin.org/get', proxies=proxies)