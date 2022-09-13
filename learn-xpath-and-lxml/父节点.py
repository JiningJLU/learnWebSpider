from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取href属性为link4.html的a节点的父亲的class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 另一种写法
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)