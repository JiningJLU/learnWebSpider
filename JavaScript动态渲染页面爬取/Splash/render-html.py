import requests
url = 'http://localhost:8050/render.html?url=https://www.baidu.com&awp;wait=5'
response = requests.get(url)
print(response.text)