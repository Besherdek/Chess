from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Chess_player(Base):
    __tablename__ = 'chess_players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    initials = Column(String, nullable=False)
    country = Column(String)
    elo = Column(Integer, nullable=False)
    title = Column(String)
    partitipation = relationship("Partitipation", back_populates="chess_player")

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable = False)
    city = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    min_elo = Column(Integer, nullable=False)
    max_elo = Column(Integer)
    partitipation = relationship("Partitipation", back_populates="tournament")

class Partitipation(Base):
    __tablename__ = "partitipations"

    id = Column(Integer, primary_key=True)
    chess_player_id = Column(Integer, ForeignKey('chess_players.id'), nullable=False)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'), nullable=False)
    partition_number = Column(Integer, nullable=False)
    place = Column(Integer, nullable=False)
    chess_player = relationship("Chess_player", back_populates="partitipation")
    tournament = relationship("Tournament", back_populates="partitipation")