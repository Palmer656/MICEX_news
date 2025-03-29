from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from db.database import sync_engine
from db.models import micex_news

app = FastAPI()

# engine = create_engine('postgresql://postgres:postgres@db:5432/events')
Session = sessionmaker(bind=sync_engine)
session = Session()

# Получаем данные
results = session.query(micex_news).filter(micex_news.c.id == 2).all()
print(results)
# result_dict = {key: value for key, value in results}
# print(result_dict)
# for result in results:
#     print(result)


@app.get("/")
def news():
    with Session() as session:
        results = session.query(micex_news).all()
        result_dict = {key: value for key, value in results}
        return {"news": result_dict}

@app.get("/id/{id}")
def get_news_by_id(id):
    with Session() as session:
        results = session.query(micex_news).filter(micex_news.c.id == int(id)).all()
        result_dict = {key: value for key, value in results}
        return {"news": result_dict}

@app.get("/ticker/{ticker}")
def get_news_by_ticker(ticker):
    with Session() as session:
        results = session.query(micex_news).filter(micex_news.c.message == ticker.upper()).all()
        result_dict = {key: value for key, value in results}
        return {"news": result_dict}



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