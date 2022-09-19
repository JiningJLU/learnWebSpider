import requests

url = 'https://spa1.scrape.center/'
html = requests.get(url).text
print(html)
