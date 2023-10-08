#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
messages = []
for i in range(10000):
    message = f'Message number {i}'
    messages.append(message)
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent Message number {i}")
print(f"Sent {len(messages)} messages")

connection.close()