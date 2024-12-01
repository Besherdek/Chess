from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

# def create_chess_player(db: Session, initials: str, elo: int, country: str = None, title: str = None):
#     db_chess_player = models.Chess_player(
#         initials = initials,
#         country = country,
#         elo = elo,
#         title = title
#     )
#     db.add(db_chess_player)
#     db.commit()
#     db.refresh(db_chess_player)
#     return db_chess_player

def create_chess_player(db: Session, db_chess_player_data: schemas.Chess_Player_Create):
    db_chess_player = models.Chess_player(**db_chess_player_data.dict())
    db.add(db_chess_player)
    db.commit()
    db.refresh(db_chess_player)
    return db_chess_player

def create_tournament(db: Session, db_tournament_data: schemas.Tournament_Create):
    db_tournament = models.Tournament(**db_tournament_data.dict())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def create_chess_player(db: Session, db_tournament_data: schemas.Chess_PLayer_Create):
    db_tournament = models.Tournament(**db_chess_player_data.dict())
    db.add(db_chess_player)
    db.commit()
    db.refresh(db_chess_player)
    return db_chess_player

def create_partitipation(db: Session, chess_player_id: int, tournament_id: int, partition_number: int, place: int):
    db_partitipation = models.Partitipation(
        chess_player_id = chess_player_id,
        tournament_id = tournament_id,
        partition_number = partition_number,
        place = place
    )
    db.add(db_partitipation)
    db.commit()
    db.refresh(db_partitipation)
    return db_partitipation

def read_chess_players(db: Session):
    return db.query(models.Chess_player).all()

def read_tournaments(db: Session):
    return db.query(models.Tournament).all()

def read_partitipations(db: Session):
    return db.query(models.Partitipation).all()

def update_chess_player(db: Session, id: int, initials: str = ..., country: str = ..., elo: int = ..., title: str = ...):
    db_chess_player = db.query(models.Chess_player).filter(models.Chess_player.id == id).first()

    if not db_chess_player:
        return None

    if initials is not ...:
        db_chess_player.initials = initials
    if country is not ...:
        db_chess_player.country = country
    if elo is not ...:
        db_chess_player.elo = elo
    if title is not ...:
        db_chess_player.title = title

    db.commit()
    db.refresh(db_chess_player)

    return db_chess_player

def update_tournament(db: Session, id: int, country: str = ..., city: str = ..., start_date: date = ..., title: str = ..., min_elo: int = ..., max_elo: int = ...):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == id).first()

    if not db_tournament:
        return None

    if country is not ...:
        db_tournament.country = country
    if city is not ...:
        db_tournament.city = city
    if start_date is not ...:
        db_tournament.start_date = start_date
    if title is not ...:
        db_tournament.title = title
    if min_elo is not ...:
        db_tournament.min_elo = min_elo
    if max_elo is not ...:
        db_tournament.max_elo = max_elo

    db.commit()
    db.refresh(db_tournament)

    return db_tournament

def update_partitipation(db: Session, id: int, chess_player_id: int = ..., tournament_id: int = ..., partition_number: int = ..., place: int = ...):
    db_partitipation = db.query(models.Partitipation).filter(models.Partitipation.id == id).first()

    if not db_partitipation:
        return None

    if chess_player_id is not ...:
        db_partitipation.chess_player_id = chess_player_id
    if tournament_id is not ...:
        db_partitipation.tournament_id = tournament_id
    if partition_number is not ...:
        db_partitipation.partition_number = partition_number
    if place is not ...:
        db_partitipation.place = place

    db.commit()
    db.refresh(db_partitipation)

    return db_partitipation

def delete_chess_player(db: Session, id: int):
    db_chess_player = db.query(models.Chess_player).filter(models.Chess_player.id == id).first()

    if not db_chess_player:
        return False

    db.delete(db_chess_player)
    db.commit()

    return True

def delete_tournament(db: Session, id: int):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == id).first()

    if not db_tournament:
        return False

    db.delete(db_tournament)
    db.commit()

    return True

def delete_partitipation(db: Session, id: int):
    db_partitipation = db.query(models.Partitipation).filter(models.Partitipation.id == id).first()

    if not db_partitipation:
        return False

    db.delete(db_partitipation)
    db.commit()

    return True