from sqlalchemy.orm import Session
import models, schemas
from datetime import date

def create_chess_player(db: Session, db_chess_player_data: schemas.Chess_Player_Create):
    db_chess_player = models.Chess_player(**db_chess_player_data.model_dump())
    db.add(db_chess_player)
    db.commit()
    db.refresh(db_chess_player)
    return db_chess_player

def create_tournament(db: Session, db_tournament_data: schemas.Tournament_Create):
    db_tournament = models.Tournament(**db_tournament_data.model_dump())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def create_partitipation(db: Session, db_partitipation_data: schemas.Partitipation_Create):
    db_partitipation = models.Tournament(**db_partitipation_data.model_dump())
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


def update_chess_player(db: Session, id: int, db_chess_player_data: schemas.Chess_Player_Update):
    db_chess_player = db.query(models.Chess_player).filter(models.Chess_player.id == id).first()
    
    if not db_chess_player:
        return None 

    db_chess_player_data = db_chess_player_data.model_dump(exclude_none=True)

    for key, val in db_chess_player_data.items():
        setattr(db_chess_player, key, val)

    db.commit()
    db.refresh(db_chess_player)
    return db_chess_player

def update_tournament(db: Session, id: int, db_tournament_data: schemas.Tournament_Update):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == id).first()
    
    if not db_tournament:
        return None

    db_tournament_data = db_tournament_data.model_dump(exclude_none=True)

    for key, val in db_tournament_data.items():
        setattr(db_tournament, key, val)

    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def update_partitipation(db: Session, id: int, db_partitipation_data: schemas.Partitipation_Update):
    db_partitipation = db.query(models.Partitipation).filter(models.Partitipation.id == id).first()
    
    if not db_partitipation:
        return None

    db_partitipation_data = db_partitipation_data.model_dump(exclude_none=True)

    for key, val in db_partitipation_data.items():
        setattr(db_partitipation, key, val)

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