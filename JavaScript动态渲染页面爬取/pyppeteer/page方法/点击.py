import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await asyncio.sleep(3)
    # 第一个参数是选择器
    await page.click('.item .name', options={
        'button': 'left',
        'clickCount': 1,
        'delay': 1000,
    })
    await browser.close()


asyncio.run(main())