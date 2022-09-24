from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 由于我只下载了Chrome浏览器的驱动，所以只能用Chrome浏览器
browser = webdriver.Chrome()
browser = webdriver.Ie()
browser = webdriver.Safari()
browser = webdriver.Edge()

try:
    browser.get('https://www.baidu.com')
    input = browser.find_element(By.ID, 'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()