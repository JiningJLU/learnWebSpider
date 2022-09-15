html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list') 
# 查找子孙节点用find方法， 只查找子节点可以用children方法
childs = items.find('li')
print(childs)
print(type(childs))

childs = items.children('li')
for child in childs.items():
    # 用这种方法获取属性
    print(child.attr('class'))

# 筛选时可以将筛选条件 作为参数传入
print(items.children('.active'))

# parent方法找到的是直接父节点。祖先节点可以用parents方法
container = items.parent()
print(container)

li = doc('.list .item-0.active')
print(li.siblings())

# doc方法返回的可能是一个节点，也可能是多个节点，但始终是一个PyQuery对象
# 如果是多个节点，想要遍历的话（因为不是像其他库一样返回list），可以用items方法，得到生成器
# 如果是多个节点，获取属性时，如果需要所有属性，需要遍历。如果只需要第一个节点的属性，直接调用attr即可。
for sibling in li.siblings().items():
    print(sibling, type(sibling))

a = doc('.item-0.active a')
print(a)
# 纯文本
print(a.text())
# 包含html
print(a.html())

# 对多个节点的对象来说，调用text()会把多个节点的text合并起来。但调用html()方法不会合并！
# 所以要提取text信息的话，不需要遍历。提取html信息的话，需要遍历。