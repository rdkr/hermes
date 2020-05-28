import sys

from sqlalchemy import create_engine
from datetimerange import DateTimeRange

sys.path.append(".")
from scheduler.sql import PlayerDB, Base


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine("sqlite:///sqlalchemy_example.db")

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# db = PlayerDB()
# db.add_time('nel', DateTimeRange("2020-05-22T10:00:00", "2020-05-22T15:00:00"))
# db.get_players()
