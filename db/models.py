from sqlalchemy import Table, Column, Integer, String, Date, Time, MetaData
from sqlalchemy.dialects.postgresql import ARRAY


metadata_obj = MetaData()


micex_news = Table(
    "MICEX_news",
    metadata_obj,
Column("id", Integer, primary_key=True),
    Column("telegram_msg_id", Integer),
    Column("date", Date),
    Column("time", Time),
    Column("tags", ARRAY(String)),
    Column("text", String),
)
