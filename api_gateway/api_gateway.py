from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from db.database import sync_engine
from db.models import micex_news
from pprint import pprint

app = FastAPI()

# engine = create_engine('postgresql://postgres:postgres@db:5432/events')
Session = sessionmaker(bind=sync_engine)
session = Session()

# Получаем данные
# results = session.query(micex_news).filter(micex_news.c.id == 2).all()


# results = session.query(micex_news).all()
# result_dict = {}
# for item in results:
#     result_dict[item[0]] = {"telegram_id": item[1],
#                             "date": item[2],
#                             "time": item[3],
#                             "tags": item[4],
#                             "text": item[5]}
# pprint(result_dict)



# result_dict = {key: value for key, value in results}
# print(result_dict)
# for result in results:
#     print(result)

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

# @app.get("/news")
# async def get_news():
#     session = Session()
#     events = session.query(Event).all()
#     return events

# @app.get("/news")
# async def get_news():
#     with sync_engine.connect() as conn:
#             query = news.select()
#             results = await database.fetch_all(query=query)
#             return [{"id": row.id, "title": row.title, "content": row.content}
#                     for row in results]