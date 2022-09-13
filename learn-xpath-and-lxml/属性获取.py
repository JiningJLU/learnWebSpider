from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 获取属性。注意获取不用加[]，中括号是匹配的时候加的。
result = html.xpath('//li/a/@href')
print(result)
