from collections import defaultdict
from concurrent import futures
from datetime import datetime
from os import environ
from random import choice
from string import ascii_letters, digits

import logging

import grpc

import hermes_pb2_grpc
import hermes_pb2

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, autoincrement=True)
    player_dc_id = Column(String, unique=True)
    player_name = Column(String)
    player_tz = Column(String, nullable=False)
    magic_token = Column(String, unique=True)

    def __repr__(self):
        return f"Player(player_id={self.player_id}, player_name={self.player_name})"


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_dc_id = Column(String, unique=True)
    event_name = Column(String)
    min_players = Column(Integer)
    min_time = Column(Float)


class Timerange(Base):
    __tablename__ = "timeranges"

    timerange_id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    tz = Column(String, nullable=False)

    player = relationship(Player)
    event = relationship(Event)

    def datetimerange(self):
        return DateTimeRange(
            datetime.fromtimestamp(self.start, timezone(self.tz)),
            datetime.fromtimestamp(self.end, timezone(self.tz)),
        )


class EventPlayers(Base):
    __tablename__ = "event_players"

    event_player_id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)

    # player = relationship(Player)
    # event = relationship(Event)


class EventDb(hermes_pb2_grpc.EventDb):
    def __init__(self, engine):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def GetMagicToken(self, request, context):
        magic_token = "".join(choice(ascii_letters + digits) for _ in range(64))
        self.session.query(Player).filter(
            Player.player_dc_id == request.player_dc_id
        ).update({"magic_token": magic_token})
        self.session.commit()
        return hermes_pb2.GetMagicTokenResponse(magic_token=magic_token)

    def GetEvents(self, request, context):
        events = self.session.query(Event).all()
        events_list = []
        for event in events:
            events_list.append(
                hermes_pb2.EventInfo(
                    event_id=event.event_id,
                    event_dc_id=event.event_dc_id,
                    event_name=event.event_name,
                    min_players=event.min_players,
                    min_time=event.min_time,
                )
            )
        return hermes_pb2.GetEventsResponse(events=events_list)

    def GetEventPlayers(self, request, context):

        now = int(datetime.utcnow().timestamp())
        players = defaultdict(list)

        result = (
            self.session.query(Player.player_dc_id, Timerange)
            .join(Timerange)
            .filter(Timerange.event_id == request.event_id)
            .filter(Timerange.end > now)
            .order_by(Timerange.start.asc())
            .all()
        )

        for player_dc_id, timerange in result:
            players[player_dc_id].append(timerange)

        player_response = []
        for player_dc_id, timeranges in players.items():

            timeranges_response = []
            for timerange in timeranges:
                timeranges_response.append(
                    hermes_pb2.Timerange(
                        id=timerange.timerange_id,
                        start=timerange.start,
                        end=timerange.end,
                        tz=timerange.tz,
                    )
                )

            player_response.append(
                hermes_pb2.GetEventPlayersResponsePlayer(
                    player_dc_id=player_dc_id,
                    timeranges=timeranges_response,
                )
            )

        return hermes_pb2.GetEventPlayersResponse(players=player_response)

    def SyncEventPlayers(self, request, context):

        channel_ids_to_event_id = {}

        session = self.sessionmaker(autoflush=False)
        session.query(EventPlayers).delete()

        for x in request.event_players:
            logging.info("{x}")

            try:
                player = (
                    session.query(Player)
                    .filter(Player.player_dc_id == x.player_id)
                    .one()
                )
                player.player_name = x.player_name
            except exc.NoResultFound:
                player = Player(
                    player_dc_id=x.player_id,
                    player_name=x.player_name,
                    player_tz="Etc/UTC",
                )

            session.merge(player)
            player_id = player.player_id

            logging.info(f"sssssss {x.channel_id}")

            if x.channel_id not in channel_ids_to_event_id.keys():

                logging.info(f"sssssss {x.channel_id}")

                try:
                    event = (
                        session.query(Event)
                        .filter(Event.event_dc_id == x.channel_id)
                        .one()
                    )
                    event.event_name = event_name = f"{x.guild_name} / {x.channel_name}"
                except exc.NoResultFound:
                    event = Event(
                        event_dc_id=x.channel_id,
                        event_name=f"{x.guild_name} / {x.channel_name}",
                    )
                    logging.info(f"zzzz made {event}")

                session.merge(event)
                event_id = event.event_id

                channel_ids_to_event_id[x.channel_id] = event_id

            session.add(EventPlayers(event_id=event_id, player_id=player_id))

        session.commit()

        return hermes_pb2.Empty()


def serve():
    from os import environ  # todo move

    engine = create_engine(
        f"postgresql://{environ['DB_USER']}:{environ['DB_PW']}@{environ['DB_HOST']}/postgres",
        echo=True,
    )
    engine.connect()
    logging.info("db conneced")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:50051")

    hermes_pb2_grpc.add_EventDbServicer_to_server(EventDb(engine), server)

    server.start()
    logging.info("grpc server started")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()
