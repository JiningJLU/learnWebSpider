import requests

data = {
    'age': 25,
    'name': 'germey'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/ 537.36',
    'Cookies': 'just some useless words, to demonstrate how to add Cookie'
}

resp = requests.get('https://www.httpbin.org/get', params=data, headers=headers)
print(resp.text)
print()
print(resp.json())
print(type(resp.json()))