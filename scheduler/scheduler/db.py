from collections import defaultdict
from datetime import datetime
from os import environ

from datetimerange import DateTimeRange
from pytz import timezone

import grpc.experimental.aio
import proto.hermes_pb2
import proto.hermes_pb2_grpc


class PlayerDB:
    async def get_players(self, event_id):
        async with grpc.aio.insecure_channel(environ["EVENT_DB_ENDPOINT"]) as channel:
            stub = proto.hermes_pb2_grpc.EventDbStub(channel)
            response = await stub.GetEventPlayers(
                proto.hermes_pb2.GetEventPlayersRequest(event_id=event_id)
            )

            result = defaultdict(list)
            for player in response.players:
                for timerange in player.timeranges:
                    result[str(player.player_dc_id)].append(
                        DateTimeRange(
                            datetime.fromtimestamp(
                                timerange.start, timezone(timerange.tz)
                            ),
                            datetime.fromtimestamp(
                                timerange.end, timezone(timerange.tz)
                            ),
                        )
                    )

            return result

    async def get_events(self):
        async with grpc.aio.insecure_channel(environ["EVENT_DB_ENDPOINT"]) as channel:
            stub = proto.hermes_pb2_grpc.EventDbStub(channel)
            response = await stub.GetEvents(proto.hermes_pb2.Empty())
            return response.events

    async def get_magic_token(self, player_dc_id):
        async with grpc.aio.insecure_channel(environ["EVENT_DB_ENDPOINT"]) as channel:
            stub = proto.hermes_pb2_grpc.EventDbStub(channel)
            response = await stub.GetMagicToken(
                proto.hermes_pb2.GetMagicTokenRequest(player_dc_id=str(player_dc_id))
            )
            return response.magic_token

    async def sync_event_players(self, event_players):

        response_list = []
        for event_player in event_players:
            response_list.append(
                proto.hermes_pb2.SyncEventPlayerRequestEventPlayers(**event_player)
            )

        async with grpc.aio.insecure_channel(environ["EVENT_DB_ENDPOINT"]) as channel:
            stub = proto.hermes_pb2_grpc.EventDbStub(channel)
            await stub.SyncEventPlayers(
                proto.hermes_pb2.SyncEventPlayerRequest(event_players=response_list)
            )
