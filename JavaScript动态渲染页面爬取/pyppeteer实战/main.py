import logging
from pyppeteer import launch
from pyppeteer.errors import TimeoutError
import asyncio
import json
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'

TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
HEADLESS = False

browser, tab = None, None


RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


async def save_data(data):
    name = data.get('name')
    file_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(file_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


async def init():
    global browser, tab
    browser = await launch(headless=HEADLESS, args=['--disable-infobars',
                                                    f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={'timeout': TIMEOUT * 1000})
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)


async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('detail data %s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()


async def scrape_detail(url):
    await scrape_page(url, 'h2')


async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.textContent')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.textContent)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.textContent')
    drama = await tab.querySelectorEval('.drama p', 'node => node.textContent')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())