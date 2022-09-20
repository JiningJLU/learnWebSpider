import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOTAL_NUMBER = 100
URL = 'https://www.httpbin.org/delay/5'

start_time = time.time()
for _ in range (1, TOTAL_NUMBER + 1):
    logging.info('scraping %s', URL)
    response = requests.get(URL)

end_time = time.time()
logging.info('total time: %s', end_time - start_time)