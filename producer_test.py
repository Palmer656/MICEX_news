import asyncio
import json
import random
from aiokafka import AIOKafkaProducer
from pprint import pprint
from test_data import cleared_messages

import config

# pprint(cleared_messages)

def serializer(value):
    """
    Обмен данными происходит в байтах, поэтому мы должны
    сначала перевести наше значение JSON, а затем в байты
    """
    return json.dumps(value).encode()


async def produce():
    producer = AIOKafkaProducer(
        bootstrap_servers=f'{config.HOST}:{config.PORT}',
        value_serializer=serializer,
        compression_type="gzip"
    )
    await producer.start()
    try:
        # while True:
        for msg in cleared_messages:
            # data = {
            #     "temp": random.randint(10, 20),
            #     "weather": random.choice(("rainy", "sunny"))
            # }
            # await producer.send(config.WEATHER_TOPIC, msg)
            await producer.send(config.MICEX_NEWS_TOPIC, msg)
            await asyncio.sleep(random.randint(3, 7))
    finally:
        await producer.stop()


if __name__ == '__main__':
    asyncio.run(produce())