from collections import defaultdict
from datetime import datetime
from os import environ
from random import choice
from string import ascii_letters, digits

from datetimerange import DateTimeRange
from pytz import timezone

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

    player = relationship(Player)
    event = relationship(Event)


class PlayerDB:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql://{environ['DB_USER']}:{environ['DB_PW']}@{environ['DB_HOST']}:5432/postgres"
        )
        self.session = sessionmaker(bind=self.engine)()
        self.event_players = None

    def get_players(self, event_id):
        now = int(datetime.utcnow().timestamp())
        players = defaultdict(list)
        result = (
            self.session.query(Player.player_id, Timerange)
            .join(Timerange)
            .filter(Timerange.event_id == str(self.event_dc_id_to_event_id(event_id)))
            .filter(Timerange.end > now)
            .order_by(Timerange.start.asc())
            .all()
        )
        for player_id, timerange in result:
            players[self.player_id_to_player_name(player_id)].append(timerange)
        return players

    def sync_event_players(self, event_players):

        self.session.query(EventPlayers).delete()

        for item in event_players:

            try:
                event_id = self.event_dc_id_to_event_id(item[0])
            except KeyError:
                event = Event(event_dc_id=item[0], event_name=f"{item[1]}/{item[2]}")
                self.session.add(event)
                self.session.commit()
                event_id = event.event_id

            try:
                player_id = self.player_dc_id_to_player_id(item[3])
            except KeyError:
                player = Player(
                    player_dc_id=item[3], player_name=item[4], player_tz="Etc/UTC"
                )
                self.session.add(player)
                self.session.commit()
                player_id = player.player_id

            self.session.merge(EventPlayers(event_id=event_id, player_id=player_id))
            self.session.commit()

    def get_magic_token(self, player_dc_id):
        chars = ascii_letters + digits
        magic_token = "".join(choice(chars) for _ in range(64))
        self.session.merge(
            Player(
                player_id=self.player_dc_id_to_player_id(player_dc_id),
                magic_token=magic_token,
            )
        )
        self.session.commit()
        return magic_token

    def player_dc_id_to_player_id(self, player_dc_id):
        try:
            return (
                self.session.query(Player.player_id)
                .filter(Player.player_dc_id == str(player_dc_id))
                .one()
                .player_id
            )
        except exc.NoResultFound:
            raise KeyError

    def event_dc_id_to_event_id(self, event_dc_id):
        try:
            return (
                self.session.query(Event.event_id)
                .filter(Event.event_dc_id == str(event_dc_id))
                .one()
                .event_id
            )
        except exc.NoResultFound:
            raise KeyError

    def player_id_to_player_name(self, player_id):
        try:
            return (
                self.session.query(Player.player_name)
                .filter(Player.player_id == player_id)
                .one()
                .player_name
            )
        except exc.NoResultFound:
            raise KeyError
