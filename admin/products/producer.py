import json
import pika
import os

AMQPS_KEY = os.environ.get('AMQPS_KEY')

params = pika.URLParameters(AMQPS_KEY)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
	print(method)
	props = pika.BasicProperties(method)
	channel.basic_publish(exchange='', routing_key='Flask', properties=props, body=json.dumps(body))