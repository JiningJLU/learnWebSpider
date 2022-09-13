from lxml import etree

htmlObject = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(htmlObject)
print(result.decode('utf-8'))
