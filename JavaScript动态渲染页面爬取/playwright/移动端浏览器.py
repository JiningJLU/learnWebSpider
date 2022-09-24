from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_12_pro_max = p.devices["iPhone 12 Pro Max"]
    browser = p.webkit.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(**iphone_12_pro_max, locale='zh-CN', timezone_id='Asia/Shanghai')
    page = context.new_page()
    page.goto('https://www.whatismybrowser.com/')
    page.wait_for_load_state(state='networkidle')
    page.screenshot(path='browser-iphone.png')
    browser.close()