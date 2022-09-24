import asyncio
from pyppeteer import launch

width, height = 1920, 1080


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot({'path': 'example.png'})
    dimensions = await page.evaluate('''
        () => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }
    ''')
    print(dimensions)
    await browser.close()


asyncio.run(main())