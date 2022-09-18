import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True, arguments={
    'x-max-priority': MAX_PRIORITY,
})

while True:
    data, pri = input().split()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=data,
                          properties=pika.BasicProperties(
                              priority=int(pri),
                              delivery_mode=2,  # make message persistent
                          ))
    print(f'Put {data}')