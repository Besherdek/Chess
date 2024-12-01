from pydantic import BaseModel
from typing import Optional
from datetime import date

class Chess_Player_Create(BaseModel):
    initials: str
    country: Optional[str] = None
    elo: int
    title: Optional[str] = None

class Chess_Player_Response(BaseModel):
    id: int
    initials: str
    country: Optional[str] = None
    elo: int
    title: Optional[str] = None

    class Config:
        orm_mode = True

class Chess_Player_Update(BaseModel):
    initials: Optional[str] = None
    country: Optional[str] = None
    elo: Optional[int] = None
    title: Optional[str] = None


class Tournament_Create(BaseModel):
    country: str
    city: str
    start_date: date
    title: str
    min_elo: int
    max_elo: int

class Tournament_Response(BaseModel):
    id: int
    country: str
    city: str
    start_date: date
    title: str
    min_elo: int
    max_elo: int

    class Config:
        orm_mode = True

class Tournament_Update(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    start_date: Optional[date] = None
    title: Optional[str] = None
    min_elo: Optional[int] = None
    max_elo: Optional[int] = None


class Partitipation_Create(BaseModel):
    chess_player_id: int
    tournament_id: int
    partition_number: int
    place: int

class Partitipation_Response(BaseModel):
    id: int
    chess_player_id: int
    tournament_id: int
    partition_number: int
    place: int

    class Config:
        orm_mode = True

class Partitipation_Update(BaseModel):
    chess_player_id: Optional[int] = None
    tournament_id: Optional[int] = None
    partition_number: Optional[int] = None
    place: Optional[int] = None