from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()


micex_news = Table(
    "MICEX_news",
    metadata_obj,
Column("id", Integer, primary_key=True),
    Column("message", String),
)