from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname()}

producer = Producer(conf)
topic = "kafka-auto-topic"

producer.produce(topic, key="456", value="counting 456")

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.flush()
