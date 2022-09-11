import requests


r = requests.get('https://ssr1.scrape.center')

print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
# history是访问历史
print(type(r.history), r.history)