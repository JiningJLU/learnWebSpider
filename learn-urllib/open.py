import socket
from urllib import request, parse
import urllib.request
import urllib.error


# 1. 最基本的例子
# response = urllib.request.urlopen('https://www.python.org')

# 2. 指定data。data本身是可选的，指定了就是post请求。
# 在这个例子中， 使用bytes把字符串转成字节。注意bytes方法需要字符串，因此我们用encode方法先把hashmap转换成字符串。

# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://httpbin.org/post', data=data)

# 3. 指定超时时间并尝试catch
# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.05)
#     print(type(response))
#     print(response.status)
#     print(response.getheaders())
#     print(response.getheader('Server'))
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('超时！')

# 4. 自己构造简单的request类对象的demo
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 5. 自己构造复杂request类对象的demo
# url = 'https://www.httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; WindowsNT)',
#     'Host': 'www.httpbin.org'
# }
# dict = {'name': 'germey'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


