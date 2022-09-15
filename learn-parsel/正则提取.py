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
result = selector.css('.item-0').re('link.*')
print(result)

# 如果re之前已经获取到了节点的纯文本值，则re方法就会只针对文本值
result = selector.css('.item-0 *::text').re('.*?item')
print(result)

# 可以用re_first方法来获取第一个符合规则的结果
result = selector.css('.item-0').re_first('<span class="bold">(.*)</span>')
print(result)