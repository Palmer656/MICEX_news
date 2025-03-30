from sqlalchemy import text, insert
from db.database import sync_engine
from db.models import metadata_obj, micex_news
from test_data import cleared_messages


def create_tables():
    metadata_obj.create_all(sync_engine)


def drop_tables():
    metadata_obj.drop_all(sync_engine)


def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(micex_news).values(cleared_messages)
        conn.execute(stmt)
        conn.commit()