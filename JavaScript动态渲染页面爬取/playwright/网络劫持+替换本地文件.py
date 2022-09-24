from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def modify_request(route, request):
        route.fulfill(path="./custom_response.html")


    page.route('/', modify_request)
    page.goto("https://spa6.scrape.center/")
    # 等两秒钟看看效果
    page.wait_for_timeout(2000)
    browser.close()

