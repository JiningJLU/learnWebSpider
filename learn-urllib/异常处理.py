from urllib import request, error

try:
    # 一个不存在的url
    resposne = request.urlopen('https://cuiqingcai.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully!')


# 返回的error.reason不一定是字符串。比如最开始的例子，链接超时，返回的就是个对象。