from kafka import KafkaConsumer
import json
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    timestamp = Column(DateTime)
    value = Column(Float)

engine = create_engine('postgresql://postgres:postgres@db:5432/events')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

consumer = KafkaConsumer(
    'events',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group_1',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    session = Session()
    event = Event(
        event_id=message.value['id'],
        timestamp=message.value['timestamp'],
        value=message.value['value']
    )
    session.add(event)
    session.commit()
