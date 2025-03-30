from sqlalchemy import delete, insert

from db.database import sync_engine
from db.models import metadata_obj, micex_news
from test_data import cleared_messages


def create_tables():
    metadata_obj.create_all(sync_engine)


def drop_tables():
    metadata_obj.drop_all(sync_engine)


def clear_tables(table):
    with sync_engine.connect() as conn:
        stmt = delete(table)
        conn.execute(stmt)
        conn.commit()


def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(micex_news).values(cleared_messages)
        conn.execute(stmt)
        conn.commit()


def insert_message(msg):
    with sync_engine.connect() as conn:
        stmt = insert(micex_news).values(msg)
        conn.execute(stmt)
        conn.commit()