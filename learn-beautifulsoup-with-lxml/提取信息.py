html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie </a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 获取名称
print(soup.title.name)

# 获取属性，如id class
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 简写也可以。注意返回的结果可能是string 也可能是list
print(soup.p['name'])
print(soup.p['class'])

# 获取内容
print(soup.p.string)

# 嵌套选择。就是一直.a.b.c.d
print(soup.body.p)
