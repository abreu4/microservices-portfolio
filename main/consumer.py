import pika
import os

AMQPS_KEY = os.environ.get('AMQPS_KEY')

params = pika.URLParameters(AMQPS_KEY)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='Flask')

def callback(ch, method, properties, body):
	print("Received in Flask")
	print(f"AMQPS_KEY: {AMQPS_KEY}")
	print(body)

channel.basic_consume(queue='Flask', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()
channel.close()