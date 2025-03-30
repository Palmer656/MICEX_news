from sqlalchemy import create_engine
from db.config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)