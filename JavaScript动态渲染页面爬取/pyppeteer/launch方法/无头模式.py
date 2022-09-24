import asyncio
from pyppeteer import launch


async def main():
    # 禁止无头模式， 关闭提示条
    await launch(headless=False, args=['--disable-infobars'])
    await asyncio.sleep(100)

asyncio.run(main())