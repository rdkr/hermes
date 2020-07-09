from os import environ
import sys

from sqlalchemy import create_engine

sys.path.append(".")
from scheduler import sql

environ["DB_USER"] = "postgres"
environ["DB_HOST"] = "localhost"

db = sql.PlayerDB()
sql.Base.metadata.create_all(db.engine)
