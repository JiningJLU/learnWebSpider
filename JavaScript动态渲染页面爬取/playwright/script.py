# created by codegen
# playwright codegen -o script.py -b firefox
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.locator("input[name=\"wd\"]").click()

    # Fill input[name="wd"]
    page.locator("input[name=\"wd\"]").fill("nba")

    # Press Enter
    page.locator("input[name=\"wd\"]").press("Enter")
    page.wait_for_url("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=nba&fenlei=256&rsv_pq=0xfc92fec10001ed8c&rsv_t=e5f8ev%2BuZixxukuTRYFOZMrj%2BeNpyO7go320r5OecW8HcBKt%2BAa8VB2RQECd&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=nba&rsp=5&inputT=1745&rsv_sug4=3802&rsv_jmp=fail")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
