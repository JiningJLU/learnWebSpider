# 和parse unparse差不多，和parse相比就是token的数量从6->5，把params放到path里了

from urllib.parse import urlsplit, urlunsplit
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)

# tuple可以用属性名/下标取内容
print(result.scheme, result[0])

data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
