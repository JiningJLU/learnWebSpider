import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, userDataDir='D:/pyppeteer/userdata', args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)


asyncio.run(main())