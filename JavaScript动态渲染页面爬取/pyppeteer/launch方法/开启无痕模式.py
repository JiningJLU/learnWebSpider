import asyncio
from pyppeteer import launch


width, height = 1920, 1080


async def main():
    browser = await launch({'headless': False, 'args': [f'--window-size={width},{height}', '--disable-infobars']})
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(2)
    await browser.close()


asyncio.run(main())