from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有li节点的a子节点
result = html.xpath('//li/a')
print(result)

# 获取所有ul节点下的子孙节点a。注意这里不能是/
result = html.xpath('//ul//a')
print(result)