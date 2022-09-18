import pika
import requests
import pickle

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape_queue'
TOTAL = 100

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)

for i in range(1, TOTAL+1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME,
                          body=pickle.dumps(request),
                          properties=pika.BasicProperties(delivery_mode=2))
    print(f'Put Request of {i}')
