from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from db.database import sync_engine
from db.models import micex_news

app = FastAPI()

Session = sessionmaker(bind=sync_engine)
session = Session()


def news_serializer(data):
    serialized_data = {}
    for item in data:
        serialized_data[item[0]] = {
            "telegram_id": item[1],
            "date": item[2],
            "time": item[3],
            "tags": item[4],
            "text": item[5]}
    return serialized_data

@app.get("/", summary="Список новостей")
def news():
    with Session() as session:
        results = session.query(micex_news).all()
        return {"messages": news_serializer(results)}

@app.get("/id/{id}", summary="Получить новость по id")
def get_news_by_id(id):
    with Session() as session:
        results = session.query(micex_news).filter(micex_news.c.id == int(id)).all()
        return {"messages": news_serializer(results)}

@app.get("/telegram_id/{telegram_id}", summary="Получить новость по id сообщения Telegram")
def get_news_by_ticker(telegram_id):
    with Session() as session:
        results = session.query(micex_news).filter(micex_news.c.telegram_msg_id == int(telegram_id)).all()
        return {"messages": news_serializer(results)}

@app.get("/tag/{tag}", summary="Получить список новостей по тэгу")
def get_news_by_ticker(tag):
    with Session() as session:
        results = session.query(micex_news).filter(micex_news.c.tags.contains([tag])).all()
        return {"messages": news_serializer(results)}
