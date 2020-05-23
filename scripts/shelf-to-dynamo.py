import shelve
import sys
import time
from decimal import Decimal

sys.path.append("../")
from scheduler import PlayerDB

s = shelve.open("shelf.bak", writeback=True)
users = {}
for name, trs in s.items():
    print(name)
    user_times = []
    for tr in trs:
        user_times.append(
            [
                Decimal(time.mktime(tr.start_datetime.timetuple())),
                Decimal(time.mktime(tr.end_datetime.timetuple())),
            ]
        )
    users[name] = user_times
s.close()

for name, times in users.items():
    print(name)
    PlayerDB().table.put_item(Item={"name": name, "times": times})
