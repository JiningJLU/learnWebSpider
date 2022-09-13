from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
# 用text函数获取文本
result = html.xpath('//li[@class="item-0"]//text()')
print(result)
