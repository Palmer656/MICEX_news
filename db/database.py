from sqlalchemy import URL, create_engine, text
from db.config import settings
# from config import t

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)

# with sync_engine.connect() as conn:
#     conn.execute()
#     conn.commit()

# print(t)