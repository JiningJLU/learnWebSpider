from cgitb import handler
import http.cookiejar, urllib.request

# 展示cookie
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')

# for item in cookie:
#     print(item.name + "=" + item.value)

filename = 'cookie.txt'
# 也可以换个格式
# cookie = http.cookiejar.MozillaCookieJar(filename)

cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)