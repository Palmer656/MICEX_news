from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()

engine = create_engine('postgresql://postgres:postgres@db:5432/events')
Session = sessionmaker(bind=engine)

@app.get("/events")
async def get_events():
    session = Session()
    events = session.query(Event).all()
    return events