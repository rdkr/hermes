from datetime import datetime
from decimal import Decimal
import time

import pytz

import boto3
from datetimerange import DateTimeRange


class PlayerDB:
    def __init__(self):
        dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
        self.table = dynamodb.Table("hermes-scheduler")

    def get_players(self):
        result = {}
        for record in self.table.scan()["Items"]:
            result[record["name"]] = get_datetimeranges(record["times"], record.get('player_timezone', 'UTC'))
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
        times = get_datetimeranges(player["Item"]["times"], player["Item"].get('player_timezone', 'UTC'))
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

    def get_tz(self, name):
        return self.table.get_item(Key={"name": name})['Item'].get('player_timezone', 'UTC')

    def set_tz(self, name, tz):
        self.table.update_item(
            Key={"name": name},
            UpdateExpression="set player_timezone = :a",
            ExpressionAttributeValues={":a": tz},
        )


def get_datetimeranges(record, timezone):
    timeranges = []
    for timerange in record:
        timeranges.append(
            DateTimeRange(
                datetime.fromtimestamp(timerange[0], pytz.timezone(timezone)),
                datetime.fromtimestamp(timerange[1], pytz.timezone(timezone)),
            )
        )
    return sorted(timeranges, key=lambda dt: dt.start_datetime)


def get_unixtimestamps(record):
    user_times = []
    for timerange in record:
        user_times.append(
            [
                Decimal(timerange.start_datetime.timestamp()),
                Decimal(timerange.end_datetime.timestamp()),
            ]
        )
    return user_times
