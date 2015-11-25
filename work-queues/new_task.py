#/usr/bin/env python
import sys
import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue to which the message will be delivered
channel.queue_declare(queue = 'task_queue', durable = True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange = '',
    routing_key = 'task_queue',
    body = message,
    properties = pika.BasicProperties(
            delivery_mode = 2, # Make message persistent
        )
    )

print " [x] Sent %r" % (message, )

connection.close()