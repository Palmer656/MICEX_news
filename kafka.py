from confluent_kafka import Producer

# Конфигурация производителя
producer = Producer({
    'bootstrap.servers': 'localhost:9092',  # адрес вашего Kafka брокера
    'api.version.request': True
})


# Функция для отправки сообщения
def send_message(topic, message):
    try:
        producer.produce(
            topic=topic,
            value=message.encode('utf-8')  # кодируем сообщение в байты
        )

        # Ждем подтверждения доставки
        producer.poll(0)
        while not producer.flush(timeout=10):
            pass
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


# Пример использования
send_message('test-topic', 'Привет, Kafka!')
