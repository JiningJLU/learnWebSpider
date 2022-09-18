import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape2'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY
})

while True:
    data, pri = input().split()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=data, properties=pika.BasicProperties(
        priority=int(pri)
    ))
    print('Sent %s with priority %s' % (data, pri))