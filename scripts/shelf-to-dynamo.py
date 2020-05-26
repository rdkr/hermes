import decimal
import shelve
import sys
import time

sys.path.append("../")
from scheduler.dynamodb import PlayerDB

s = shelve.open("shelf.bak", writeback=True)
users = {}
for name, trs in s.items():
    print(name)
    user_times = []
    for tr in trs:
        user_times.append(
            [
                decimal.Decimal(time.mktime(tr.start_datetime.timetuple())),
                decimal.Decimal(time.mktime(tr.end_datetime.timetuple())),
            ]
        )
    users[name] = user_times
s.close()

for name, times in users.items():
    print(name)
    PlayerDB().table.put_item(Item={"name": name, "times": times})
