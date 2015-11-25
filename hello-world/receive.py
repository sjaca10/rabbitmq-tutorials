#!/usr/bin/env python
import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue to which the message will be delivered
channel.queue_declare(queue = 'hello')

print ' [*] Waiting for messages. To exit press CTRL + C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body, )

channel.basic_consume(callback,
    queue = 'hello',
    no_ack = True)

channel.start_consuming()