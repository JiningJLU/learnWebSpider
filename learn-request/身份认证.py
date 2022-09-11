from urllib.request import HTTPBasicAuthHandler
import requests

r = requests.get('https://ssr3.scrape.center', auth=HTTPBasicAuthHandler('admin', 'admin'))
# 简写
r = requests.get('https://ssr3.scrape.center', auth=('admin', 'admin'))

print(r.status_code)