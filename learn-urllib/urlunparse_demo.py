# 从token构造url的方法。token数组的长度必须是6

from urllib.parse import urlunparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))