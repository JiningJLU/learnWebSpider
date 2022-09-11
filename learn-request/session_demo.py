import requests

# 每次get post相当于新开了一个浏览器，无法共享session。想共享吗？看这个

s = requests.Session()
# 使用session对象去get
s.get('https://www.httpbin.org/cookies/set/number/123456789')
r = s.get('https://www.httpbin.org/cookies')
print(r.text)