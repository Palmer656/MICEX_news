from sqlalchemy import text, insert
from db.database import sync_engine
from db.models import metadata_obj, micex_news

def get_123_sync():
    pass

def create_tables():
    # sync_engine.echo = False
    # metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    # sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(micex_news).values(
            [
                {"message": "RUAL"},
                {"message": "SBER"}
            ]
        )
        conn.execute(stmt)
        conn.commit()

def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(micex_news).values(
            [
                {"message": "RUAL"},
                {"message": "SBER"}
            ]
        )
        conn.execute(stmt)
        conn.commit()