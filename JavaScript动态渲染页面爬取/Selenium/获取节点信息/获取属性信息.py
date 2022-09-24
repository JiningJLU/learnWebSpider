from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = 'https://spa2.scrape.center'
browser.get(url)
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)
print(logo.get_attribute('src'))