from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.item'))
)

html = browser.page_source
doc = pq(html)
names = doc('.item .name').items()
for name in names:
    print(name.text())
browser.close()
