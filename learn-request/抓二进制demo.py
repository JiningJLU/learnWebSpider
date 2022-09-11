from urllib import request
import requests

r = requests.get('https://scrape.center/favicon.ico')

with open('favicon.ico', 'wb') as f:
    f.write(r.content)