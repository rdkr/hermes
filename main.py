import logging
import os

from discord.ext import commands

from scheduler import Scheduler


def main():
    logging.basicConfig(level=logging.INFO)
    bot = commands.Bot(command_prefix="$")
    bot.add_cog(Scheduler(bot))
    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    # main()
    import shelve
    import time
    import boto3

    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="http://localhost:8000")
    # table = dynamodb.create_table(
    #     TableName='Movies',
    #     KeySchema=[
    #         {
    #             'AttributeName': 'name',
    #             'KeyType': 'HASH'
    #         },
    #     ],
    #     AttributeDefinitions=[
    #         {
    #             'AttributeName': 'name',
    #             'AttributeType': 'S'
    #         },
    #     ],
    #     ProvisionedThroughput={
    #         'ReadCapacityUnits': 1,
    #         'WriteCapacityUnits': 1
    #     }
    # )
    from decimal import Decimal

    s = shelve.open("shelf", writeback=True)
    users = {}
    for name, trs in s.items():
        user_times = []
        for tr in trs:
            user_times.append([
                Decimal(time.mktime(tr.start_datetime.timetuple())),
                Decimal(time.mktime(tr.end_datetime.timetuple())),
            ])
        users[name.lower()] = user_times
    s.close()



    table = dynamodb.Table('Movies')
    for name, times in users.items():
        table.put_item(
            Item={
                'name': name,
                'times': times,
            }
        )
            # print(, tr.end_datetime)

