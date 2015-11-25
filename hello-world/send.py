#!/usr/bin/env python
import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue to which the message will be delivered
channel.queue_declare(queue = 'hello')

# Send a message
channel.basic_publish(exchange = '',
    routing_key = 'hello',
    body = 'Hello World!')

print " [x] Sent 'Hello World!'"

connection.close()