from playwright.sync_api import sync_playwright


# 创建Page对象后，就开始监听response事件。回调方法名设置为on_response
def on_response(response):
    print(f'Statue {response.status}: {response.url}')


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # 注册监听事件
    page.on('response', on_response)
    page.goto("https://spa6.scrape.center/")
    page.wait_for_load_state('networkidle')
    # 获取网页源代码
    print(page.content())



    page.goto("https://spa6.scrape.center/")
    page.wait_for_load_state('networkidle')
    # 获取节点属性。第一个参数是选择器，第二个参数是属性名
    print(page.get_attribute('a.name', 'href'))
    # 获取多个节点
    elements = page.query_selector_all('a.name')
    for element in elements:
        print(element.get_attribute('href'))
        # 获取节点文本
        print(element.text_content())
    # 获取单个节点
    element = page.query_selector('a.name')
    print(element.get_attribute('href'))
    print(element.text_content())
    browser.close()