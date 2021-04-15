#!/usr/bin/python

# -*- coding: utf-8 -*-
import pika, yaml, base64, time

log_file = open("/var/log/my_project/receiver/receiver.log","a")
config_file = open("/etc/my_project/receiver/receiver.yaml","r")
config = yaml.load(config_file)

pika_username = config["rabbitmq"]["username"]
pika_password = base64.b64decode(config["rabbitmq"]["password"])
pika_addr = config["rabbitmq"]["host"]
pika_port = config["rabbitmq"]["port"]
pika_virtualhost = config["rabbitmq"]["virtualhost"]
pika_queue = config["rabbitmq"]["queue"]


credentials = pika.PlainCredentials(pika_username, pika_password)
parameters  = pika.ConnectionParameters(pika_addr, pika_port, pika_virtualhost, credentials)
connection  = pika.BlockingConnection(parameters)
channel     = connection.channel()

channel.queue_declare(queue=pika_queue, durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,)) #this goes to stdout
    print("[x] Received %r" % (body,), file=log_file) #this goes to log file
    time.sleep(int(body.decode('ascii')))
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=pika_queue)

channel.start_consuming()
