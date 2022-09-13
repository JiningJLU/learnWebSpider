from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# //代表所有子孙节点
result = html.xpath('//li')
print(result)