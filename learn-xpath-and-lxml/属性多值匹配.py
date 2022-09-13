from lxml import etree

# 这段文本中，li节点有两个class，即li和li-first
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
# 获取class属性中包含li属性的节点。注意多个属性直接用空格分开这种语法是固定的。
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)