from os import environ
import sys

from sqlalchemy import create_engine

sys.path.append(".")
from scheduler import sql, dynamodb

db = sql.PlayerDB()
dynamo = dynamodb.PlayerDB()

sql.Base.metadata.create_all(create_engine(
            f"postgresql://root:{environ['DB_PW']}@{environ['DB_HOST']}:5432/hermes"
        ))

for user, times in dynamo.get_players().items():
    db.set_tz(user, dynamo.get_tz(user))
    for time in times:
        db.add_time(user, time)

# db.add_time('nel', DateTimeRange("2020-05-22T10:00:00", "2020-05-22T15:00:00"))
# db.get_players()
