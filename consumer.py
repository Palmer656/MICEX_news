import asyncio
import json
from datetime import datetime

from aiokafka import AIOKafkaConsumer

import kafka_config
from db.queries.core import insert_message


def deserializer(serialized):
    """
    Десериализатор получаемых данных
    """
    deserialized = json.loads(serialized)
    deserialized["date"] = datetime.strptime(deserialized["date"], '%Y-%m-%d').date()
    deserialized["time"] = datetime.strptime(deserialized["time"], '%H:%M:%S').time()
    return deserialized


async def event_handler(value):
    """
    Обработчик события. Как только мы получаем новое сообщение,
    будет отрабатывать данная функция
    """
    insert_message(value)


async def consume():
    consumer = AIOKafkaConsumer(
        kafka_config.MICEX_NEWS_TOPIC,
        bootstrap_servers=f'{kafka_config.HOST}:{kafka_config.PORT}',
        value_deserializer=deserializer
    )
    await consumer.start()
    try:
        async for msg in consumer:
            await event_handler(msg.value)
    finally:
        await consumer.stop()


if __name__ == '__main__':
    asyncio.run(consume())
