import pika
import os

AMQPS_KEY = os.environ.get('AMQPS_KEY')

params = pika.URLParameters(AMQPS_KEY)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
	channel.basic_publish(exchange='', routing_key='admin', body='hello')
	channel.basic_publish(exchange='', routing_key='Flask', body='hello')