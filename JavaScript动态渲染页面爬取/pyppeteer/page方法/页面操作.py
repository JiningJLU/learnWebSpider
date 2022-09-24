import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    # 提示: 下面的这些操作，由于电脑和网络速度的影响，可能会执行比较久
    # 一个操作没做完，下一个操作就开始了，所以可能会出现一些问题
    # 加一些睡眠时间，可以解决这个问题
    await page.goto('https://www.baidu.com/')
    await asyncio.sleep(3)
    await page.goto('https://spa2.scrape.center/')

    # 后退
    await page.goBack()
    await asyncio.sleep(1)
    # 前进
    await page.goForward()
    await asyncio.sleep(1)
    # 刷新
    await page.reload()
    await asyncio.sleep(1)
    # 保存PDF
    await page.pdf()
    await asyncio.sleep(1)
    # 保存截图
    await page.screenshot()
    await asyncio.sleep(1)
    # 设置页面HTML
    await page.setContent('<h2>Hello World</h2>')
    await asyncio.sleep(1)
    # 设置 User-Agent
    await page.setUserAgent('Python')
    await asyncio.sleep(1)
    # 设置headers
    await page.setExtraHTTPHeaders(headers={})
    await asyncio.sleep(1)
    # 关闭
    await page.close()
    await browser.close()


asyncio.run(main())