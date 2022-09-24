import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    page = await browser.newPage()
    await page.goto('https://www.bing.com/')
    pages = await browser.pages()
    print('Pages:', pages)
    page1 = pages[1]
    # 选中下标为1的选项卡
    await page1.bringToFront()
    # 睡眠100秒，注意单位
    await asyncio.sleep(100)


asyncio.run(main())