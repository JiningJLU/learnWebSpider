from cgitb import text
import re
html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# 按text查找，就是正则匹配
print(soup.find_all(text = re.compile('link')))