html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
'''
from parsel import Selector
selector = Selector(text=html)
items = selector.css('.item-0')
for item in items:
    # 不调用get()方法，返回的是一个SelectorList对象
    text = item.xpath('.//text()').get()
    print(text)
# 对于SelectorList对象调用get()，只会对第一个li起效果。本例中包含3个li
result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
print(result)
result = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
print(result)