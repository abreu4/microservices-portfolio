import pika
import os

AMQPS_KEY = os.environ.get('AMQPS_KEY')

params = pika.URLParameters(AMQPS_KEY)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
	print("Received in admin")
	print(f"AMQPS_KEY: {AMQPS_KEY}")
	print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print("Started consuming")

channel.start_consuming()
channel.close()