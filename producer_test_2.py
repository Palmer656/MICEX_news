from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {
        'id': random.randint(1, 1000),
        'timestamp': int(time.time()),
        'value': random.random()
    }
    producer.send('events', value=event)
    time.sleep(5)
