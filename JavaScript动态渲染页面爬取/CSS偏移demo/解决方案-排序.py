import re

from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def parse_name(name_html):
    has_whole = name_html('.whole')
    if has_whole:
        return has_whole.text()
    else:
        chars = name_html('.char').items()
        items = []
        for char in chars:
            items.append({
                'text': char.text().strip(),
                'left': int(re.search('(\d+)px', char.attr('style')).group(1))
            })
        items = sorted(items, key=lambda x: x['left'])
        return ''.join([item['text'] for item in items])

browser = webdriver.Chrome()
browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.item'))
)
html = browser.page_source
doc = pq(html)
names = doc('.item .name').items()
for name in names:
    name = parse_name(name)
    print(name)
browser.close()