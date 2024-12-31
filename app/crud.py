from sqlalchemy.orm import Session
from sqlalchemy import select, text
import models, schemas

def apply_sort(query, sort_by: str, asc: bool, valid_columns: dict):
    if sort_by not in valid_columns:
        raise ValueError(f"Invalid column name: {sort_by}")
    sort_by = valid_columns[sort_by]
    return query.order_by(sort_by.asc() if asc else sort_by.desc())


# player--------------------------------------------------------------------

def create_chess_player(db: Session, db_chess_player_data: schemas.Chess_Player_Create):
    try:
        db_chess_player = models.Chess_player(**db_chess_player_data.model_dump())
        db.add(db_chess_player)
        db.commit()
        db.refresh(db_chess_player)
    except Exception as e:
        raise ValueError(e)

def read_chess_players(db: Session, select_columns: list, min_elo: int, max_elo: int, country: str, sort_by: str, asc: bool, limit: int, offset: int):
    corresponding_columns = {
        "id": models.Chess_player.id,
        "initials": models.Chess_player.initials,
        "country": models.Chess_player.country,
        "elo": models.Chess_player.elo,
        "title": models.Chess_player.title,
        "pets": models.Chess_player.pets
    }

    if select_columns:
        select_columns = [corresponding_columns[col] for col in select_columns]

    query = select(*select_columns).limit(limit).offset(offset) if select_columns else select(models.Chess_player).limit(limit).offset(offset)

    if min_elo:
        query = query.where(models.Chess_player.elo >= min_elo)

    if max_elo:
        query = query.where(models.Chess_player.elo <= max_elo)

    if country:
        query = query.where(models.Chess_player.country == country)

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, corresponding_columns)
        except ValueError as e:
            raise ValueError(e)
        
    if select_columns:
        return db.execute(query).all()
        
    return db.execute(query).scalars().all()

def update_chess_player(db: Session, id: int, db_chess_player_data: schemas.Chess_Player_Update):
    db_chess_player = db.query(models.Chess_player).filter(models.Chess_player.id == id).first()
    
    if not db_chess_player:
        return None 

    db_chess_player_data = db_chess_player_data.model_dump(exclude_none=True)

    for key, val in db_chess_player_data.items():
        setattr(db_chess_player, key, val)

    db.commit()
    db.refresh(db_chess_player)

def delete_chess_player(db: Session, id: int):
    db_chess_player = db.query(models.Chess_player).filter(models.Chess_player.id == id).first()

    if not db_chess_player:
        return False

    db.delete(db_chess_player)
    db.commit()

    return True

def search_pets(db: Session, pet_name: str, limit: int, offset: int):
    sql = text("""
        SELECT * 
        FROM chess_players
        WHERE pets::text ILIKE :pattern
        LIMIT :limit
        OFFSET :offset
    """)
    return db.execute(sql, {"pattern": f"%{pet_name}%", "limit": limit, "offset": offset}).all()


# tournament--------------------------------------------------------------------

def create_tournament(db: Session, db_tournament_data: schemas.Tournament_Create):
    try:
        db_tournament = models.Tournament(**db_tournament_data.model_dump())
        db.add(db_tournament)
        db.commit()
        db.refresh(db_tournament)
    except Exception as e:
        raise ValueError(e)

def read_tournaments(db: Session, sort_by: str, asc: bool, limit: int, offset: int):
    query = select(models.Tournament)
    
    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "country": models.Tournament.country,
                "city": models.Tournament.city,
                "start_date": models.Tournament.start_date,
                "title": models.Tournament.title,
                "min_elo": models.Tournament.min_elo,
                "max_elo": models.Tournament.max_elo
            })
        except ValueError as e:
            raise ValueError(e)
        
    return db.execute(query).limit(limit).offset(offset).scalars().all()

def update_tournament(db: Session, id: int, db_tournament_data: schemas.Tournament_Update):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == id).first()
    
    if not db_tournament:
        return None

    db_tournament_data = db_tournament_data.model_dump(exclude_none=True)

    for key, val in db_tournament_data.items():
        setattr(db_tournament, key, val)

    db.commit()
    db.refresh(db_tournament)

def delete_tournament(db: Session, id: int):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == id).first()

    if not db_tournament:
        return False

    db.delete(db_tournament)
    db.commit()

    return True


# partitipation--------------------------------------------------------------------

def create_partitipation(db: Session, db_partitipation_data: schemas.Partitipation_Create):
    try:
        db_partitipation = models.Partitipation(**db_partitipation_data.model_dump())
        db.add(db_partitipation)
        db.commit()
        db.refresh(db_partitipation)
    except Exception as e:
        raise ValueError(e)

def read_partitipations(db: Session, sort_by: str, asc: bool, limit: int, offset: int):
    query = select(models.Partitipation)
    
    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "chess_player_id": models.Partitipation.chess_player_id,
                "tournament_id": models.Partitipation.tournament_id,
                "partition_number": models.Partitipation.partition_number,
                "place": models.Partitipation.place
            })
        except ValueError as e:
            raise ValueError(e)
        
    return db.execute(query).limit(limit).offset(offset).scalars().all()

def update_partitipation(db: Session, id: int, db_partitipation_data: schemas.Partitipation_Update):
    db_partitipation = db.query(models.Partitipation).filter(models.Partitipation.id == id).first()
    
    if not db_partitipation:
        return None

    db_partitipation_data = db_partitipation_data.model_dump(exclude_none=True)

    for key, val in db_partitipation_data.items():
        setattr(db_partitipation, key, val)

    db.commit()
    db.refresh(db_partitipation)

def update_place(db: Session, initials: str, tournament: str, place:int):
    player_subquery = db.query(models.Chess_player.id).filter(models.Chess_player.initials == initials).subquery()
    tournament_subquery = db.query(models.Tournament.id).filter(models.Tournament.title == tournament).subquery()
    
    db_partitipation = db.query(models.Partitipation).filter(
        models.Partitipation.chess_player_id == player_subquery,
        models.Partitipation.tournament_id == tournament_subquery
    ).first()

    if not db_partitipation:
        return False

    db_partitipation.place = place
    db.commit()
    db.refresh(db_partitipation)
    return True

def delete_partitipation(db: Session, id: int):
    db_partitipation = db.query(models.Partitipation).filter(models.Partitipation.id == id).first()

    if not db_partitipation:
        return False

    db.delete(db_partitipation)
    db.commit()

    return True

def read_partitipation_results(db: Session, sort_by: str, asc: bool, limit: int, offset: int):
    query = select(
        models.Chess_player.initials,
        models.Partitipation.place,
        models.Tournament.title,
    ).join(
        models.Chess_player, models.Partitipation.chess_player_id == models.Chess_player.id
    ).join(
        models.Tournament, models.Partitipation.tournament_id == models.Tournament.id
    )

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "initials": models.Chess_player.initials,
                "place": models.Partitipation.place,
                "title": models.Tournament.title
            })
        except ValueError as e:
            raise ValueError(e)
    else:
        query = query.order_by(models.Chess_player.initials)

    query = db.execute(query).limit(limit).offset(offset).all()

    return query

def read_winners(db: Session, sort_by: str, asc: bool, limit: int, offset: int):
    query = select(
        models.Chess_player.initials,
        models.Partitipation.place
    ).join(
        models.Chess_player, models.Chess_player.id == models.Partitipation.chess_player_id
    ).group_by(
        models.Partitipation.place, models.Chess_player.initials
    ).having(
        models.Partitipation.place <= 3,
        models.Partitipation.place > 0
    )

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "initials": models.Chess_player.initials,
                "place": models.Partitipation.place
            })
        except ValueError as e:
            raise ValueError(e)
        
    return db.execute(query).limit(limit).offset(offset).all()