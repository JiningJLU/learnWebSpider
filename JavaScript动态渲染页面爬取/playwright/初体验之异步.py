import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto("https://www.baidu.com")
            await page.screenshot(path=f"example-{browser_type.name}.png")
            print(await page.title())
            await browser.close()


asyncio.run(main())