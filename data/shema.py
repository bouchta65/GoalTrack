from sqlalchemy import (
    create_engine, MetaData, Table,
    Column, Integer, String, Text, TIMESTAMP, func
)

engine = create_engine("postgresql://postgres:123@localhost:5432/goaltrackdb")

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nom", String, nullable=False),
    Column("description", Text, nullable=False),
    Column("date", TIMESTAMP, server_default=func.now()),
    Column("priority", String),
    Column("status", String)
)

metadata.create_all(engine)
