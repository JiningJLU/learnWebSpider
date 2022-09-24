from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://spa2.scrape.center')
# 如果等待节点没有出现，会隐式等待10秒，然后抛出异常
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)