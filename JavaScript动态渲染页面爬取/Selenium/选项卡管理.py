import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 新开一个选项卡
browser.execute_script('window.open()')
# 查看所有选项卡
print(browser.window_handles)
# 切换到新开的选项卡
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
# 切换回第一个选项卡
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')