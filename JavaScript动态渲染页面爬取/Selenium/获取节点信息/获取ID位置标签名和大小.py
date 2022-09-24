from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = 'https://spa2.scrape.center'
browser.get(url)
title = browser.find_element(By.CLASS_NAME, 'logo-title')

print(title.id)
print(title.location)
print(title.tag_name)
print(title.size)