#!/usr/bin/env python
import time
import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue to which the message will be delivered
# The queue will be created with the durable option enabled
channel.queue_declare(queue = 'task_queue', durable = True)

print ' [*] Waiting for messages. To exit press CTRL + C '

def callback(ch, method, properties, body):
    print "[X] Received %r" % (body,)
    time.sleep(body.count('.'))
    print "[X] Done"
    # Send a proper acknowledgment from the worker once it's done with a task
    ch.basic_ack(delivery_tag = method.delivery_tag)

# Without acknowledgment enable
# channel.basic_consume(callback,
#     queue = 'hello',
#     no_ack = True)

# Quality of Service is 1 for a better loading balancer
channel.basic_qos(prefetch_count = 1)
# With acknowledgment enable
channel.basic_consume(callback,
    queue = 'task_queue')

channel.start_consuming()