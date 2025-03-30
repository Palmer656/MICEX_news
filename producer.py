import asyncio
import json
import random

from aiokafka import AIOKafkaProducer

import kafka_config
from test_data import cleared_messages


def serializer(value):
    """
    Обмен данными происходит в байтах, поэтому мы должны
    сначала перевести наше значение JSON, а затем в байты
    """
    value["date"] = value["date"].isoformat()
    value["time"] = value["time"].isoformat()
    return json.dumps(value).encode()


async def produce():
    producer = AIOKafkaProducer(
        bootstrap_servers=f'{kafka_config.HOST}:{kafka_config.PORT}',
        value_serializer=serializer,
        compression_type="gzip"
    )
    await producer.start()
    try:
        for msg in cleared_messages:
            await producer.send(kafka_config.MICEX_NEWS_TOPIC, msg)
            await asyncio.sleep(random.randint(3, 7))
    finally:
        await producer.stop()


if __name__ == '__main__':
    asyncio.run(produce())