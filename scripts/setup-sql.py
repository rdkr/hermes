from os import environ
import sys

from sqlalchemy import create_engine

sys.path.append(".")
from scheduler import sql

db = sql.PlayerDB()

sql.Base.metadata.create_all(create_engine(
    f"postgresql://root:{environ['DB_PW']}@{environ['DB_HOST']}:5432/hermes"
))
