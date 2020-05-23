from datetime import datetime
from decimal import Decimal
import time

import boto3
from datetimerange import DateTimeRange


class PlayerDB:
    def __init__(self):
        dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
        self.table = dynamodb.Table("hermes-scheduler")

    def get_players(self):
        result = {}
        for record in self.table.scan()["Items"]:
            result[record["name"]] = get_datetimeranges(record["times"])
        return result

    def add_time(self, name, timerange):
        self.table.update_item(
            Key={"name": name},
            UpdateExpression="SET times = list_append(if_not_exists(times, :empty_list), :a)",
            ExpressionAttributeValues={
                ":a": get_unixtimestamps([timerange]),
                ":empty_list": [],
            },
        )

    def delete_time(self, name, index):
        player = self.table.get_item(Key={"name": name})
        times = get_datetimeranges(player["Item"]["times"])
        del times[index]
        self.table.update_item(
            Key={"name": name},
            UpdateExpression="SET times = :a",
            ExpressionAttributeValues={":a": get_unixtimestamps(times)},
        )

    def delete_times(self, name):
        self.table.update_item(
            Key={"name": name},
            UpdateExpression="set times = :a",
            ExpressionAttributeValues={":a": []},
        )


def get_datetimeranges(record):
    timeranges = []
    for timerange in record:
        timeranges.append(
            DateTimeRange(
                datetime.fromtimestamp(timerange[0]),
                datetime.fromtimestamp(timerange[1]),
            )
        )
    return sorted(timeranges, key=lambda dt: dt.start_datetime)


def get_unixtimestamps(record):
    user_times = []
    for timerange in record:
        user_times.append(
            [
                Decimal(time.mktime(timerange.start_datetime.timetuple())),
                Decimal(time.mktime(timerange.end_datetime.timetuple())),
            ]
        )
    return user_times
