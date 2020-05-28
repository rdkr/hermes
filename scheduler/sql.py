from collections import defaultdict
from datetime import datetime
from os import environ

from datetimerange import DateTimeRange
from pytz import timezone

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, exc

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"
    id = Column(String(250), primary_key=True)
    tz = Column(String(250), nullable=False)

    def __repr__(self):
        return f"Player({self.id}, {self.tz})"


class Timerange(Base):
    __tablename__ = "timerange"
    id = Column(Integer, primary_key=True, autoincrement=True)

    player_id = Column(String(250), ForeignKey("player.id"), nullable=False)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    tz = Column(String(250), nullable=False)

    player = relationship(Player)

    def __repr__(self):
        return f"Timerange({self.id}, {self.player_id}, {self.start}, {self.end}, {self.tz})"

    def datetimerange(self):
        return DateTimeRange(
            datetime.fromtimestamp(self.start, timezone(self.tz)),
            datetime.fromtimestamp(self.end, timezone(self.tz)),
        )


class PlayerDB:
    def __init__(self):
        self.engine = create_engine(
            f"postgresql://root:{environ['DB_PW']}@{environ['DB_HOST']}:5432/hermes"
        )
        self.session = sessionmaker(bind=self.engine)()

    def get_players(self):
        players = defaultdict(list)
        for player_id, timerange in (
            self.session.query(Player.id, Timerange).join(Timerange).all()
        ):
            players[player_id].append(timerange)
        return players

    def add_time(self, player_id, timerange):
        self.session.add(
            Timerange(
                player_id=player_id,
                start=timerange.start_datetime.timestamp(),
                end=timerange.end_datetime.timestamp(),
                tz=self.get_tz(player_id),
            )
        )
        self.session.commit()

    def delete_time(self, player_id, index):
        self.session.query(Timerange).filter_by(player_id=player_id, id=index).delete()
        return self.session.commit()

    def delete_times(self, player_id):
        self.session.query(Timerange).filter_by(player_id=player_id).delete()
        self.session.commit()

    def clean_times(self):
        now = int(datetime.utcnow().timestamp())
        self.session.query(Timerange).filter(now > Timerange.end).delete()
        self.session.commit()

    def get_tz(self, player_id):
        try:
            return self.session.query(Player.tz).filter(Player.id == player_id).one().tz
        except exc.NoResultFound:
            raise KeyError

    def set_tz(self, player_id, tz):
        self.session.merge(Player(id=player_id, tz=tz))
        self.session.commit()
