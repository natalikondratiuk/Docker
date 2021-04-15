#!/usr/bin/python

# -*- coding: utf-8 -*-
import pika, yaml, base64, time, random

config_file = open("/Nata/Docker/my_project/sender/sender.yaml","r")
config = yaml.load(config_file)

pika_username = config["rabbitmq"]["username"]
pika_password = base64.b64decode(config["rabbitmq"]["password"])
pika_addr = config["rabbitmq"]["host"]
pika_port = config["rabbitmq"]["port"]
pika_virtualhost = config["rabbitmq"]["virtualhost"]
pika_queue = config["rabbitmq"]["queue"]


def send_message_rabbitmq(message="Hello World!"):
    credentials = pika.PlainCredentials(pika_username, pika_password)
    parameters = pika.ConnectionParameters(pika_addr, pika_port, pika_virtualhost, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=pika_queue, durable=True)
    channel.basic_publish(exchange='',
                          routing_key=pika_queue,
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode=2,
                          ))
    connection.close()

while True:
  send_message_rabbitmq(str(random.randint(1,7)))
  time.sleep(5)
