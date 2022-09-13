from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

html = etree.HTML(text)
# 第一个li节点的所有祖先
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 第一个li节点的所有div祖先
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 第一个li节点的所有属性
result = html.xpath('//li[1]/attribute::*')
print(result)
# 所有直接子节点中属性href="link1.html"的直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 获取所有子孙节点中的span节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 获取当前节点之后的所有节点中的第二个
result = html.xpath('//li[1]/following::*')
print(result)
# 获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)