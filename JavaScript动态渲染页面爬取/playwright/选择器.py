from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        # 文本选择
        page.click("text=百度")
        # CSS 选择器
        page.click("button")
        page.click("#nav-bar .contact-us-iitem")
        # 根据节点特定属性选择
        page.click("[data-test=login-button]")
        page.click("[aria-label='Sign in']")
        # CSS选择器+文本值
        page.click("button:has-text('Playwright')") # 包含文本即可，不需要完全匹配
        page.click("#nav-bar :text('Contact us')")  # 完全匹配，文本必须是Contact us
        # CSS选择器+节点关系
        page.click(".item-description:has(.item-promo-banner)")
        page.click("input:right-of(:text('Username'))")
        # XPath选择器
        page.click("xpath=//button")
