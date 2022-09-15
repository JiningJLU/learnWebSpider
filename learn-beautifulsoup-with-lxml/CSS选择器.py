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
# 都是CSS类选择器的写法
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

# 可以嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))
    # 还可以获取属性、文本
    print(ul['id'])
    print(ul.attrs['id'])
    for li in ul.select('li'):
        # get_text方法和string属性效果完全一致
        print('Text: ', li.get_text())
        print('String: ', li.string)