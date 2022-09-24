from selenium import webdriver

browser = webdriver.Chrome()
# browser.get('http://jqfy.jl54.org/jltw/wechat/getUserInfo?t=1663767743509')
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()