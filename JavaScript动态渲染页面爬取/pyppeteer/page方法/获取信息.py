import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    print('HTML:', await page.content())
    print('Cookies:', await page.cookies())
    await browser.close()


asyncio.run(main())