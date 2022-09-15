# 指的是选择子孙后代、父亲等等
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# contents返回直接子节点列表
print(soup.p.contents)
# children属性返回的是生成器类型的直接子节点
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# descendants可以获取所有子孙节点, 也是迭代器
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 找某个节点的父节点 用parent
print(soup.a.parent)

# 找祖先节点，用parents。注意是迭代器类型
for i, parent in enumerate(soup.a.parents):
    print(i, parent)

# 找直接兄弟节点
print(soup.a.previous_sibling)
print(soup.a.next_sibling)
# 找所有兄弟节点
for i, prev in enumerate(soup.a.previous_siblings):
    print('prev', i, prev)
for i, next in enumerate(soup.a.next_siblings):
    print('next', i, next)
