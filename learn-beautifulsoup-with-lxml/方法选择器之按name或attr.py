# findall(name, attrs, recursive, text, **kwargs)

html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul> 
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>   
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# 查询所有名字是ul的节点
print(soup.find_all(name='ul'))
# 打印类型，是Tag
print(type(soup.find_all(name='ul')[0]))

# Tag类型可以嵌套查询
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

print('还可以按attrs查找')
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

