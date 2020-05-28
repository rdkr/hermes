import os
import sys

from sqlalchemy import create_engine

sys.path.append(".")
from scheduler import sql, dynamodb


sql.Base.metadata.create_all(create_engine(os.environ["DB"]))

db = sql.PlayerDB()
dynamo = dynamodb.PlayerDB()

for user, times in dynamo.get_players().items():
    db.set_tz(user, dynamo.get_tz(user))
    for time in times:
        db.add_time(user, time)

# db.add_time('nel', DateTimeRange("2020-05-22T10:00:00", "2020-05-22T15:00:00"))
# db.get_players()
