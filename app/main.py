from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
import crud, schemas

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# player--------------------------------------------------------------------

@app.post("/chess_players/")
def create_chess_player(chess_player: schemas.Chess_Player_Create, db: Session = Depends(get_db)):
    try:
        crud.create_chess_player(db, chess_player)
        return "Player created successfully"
    except Exception as e:
        raise HTTPException(400, f"Error creating player: {e}")

@app.get("/chess_players/", response_model=list[schemas.Chess_Player_Response])
def read_chess_players(
    select_columns: Optional[List[str]] = Query(None),
    min_elo: int = None,
    max_elo: int = None,
    country: str = None,
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_chess_players(db, select_columns, min_elo, max_elo, country, sort_by, asc)

@app.put("/chess_players/{id}")
def update_chess_player(id: int, chess_player: schemas.Chess_Player_Update, db: Session = Depends(get_db)):
    try:
        crud.update_chess_player(db, id, chess_player)
        return "Player updated successfully"
    except Exception as e:
        raise HTTPException(400, f"Error updating player: {e}")

@app.delete("/chess_players/{id}")
def delete_chess_player(id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_chess_player(db, id)
        return "Player deleted successfully"
    except Exception as e:
        raise HTTPException(400, f"Error deleting player: {e}")


# tournament--------------------------------------------------------------------

@app.post("/tournaments/")
def create_tournament(tournament: schemas.Tournament_Create, db: Session = Depends(get_db)):
    try:
        crud.create_tournament(db, tournament)
        return "Tournament created successfully"
    except Exception as e:
        raise HTTPException(400, f"Error creating tournament: {e}")

@app.get("/tournaments/", response_model=list[schemas.Tournament_Response])
def read_tournaments(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_tournaments(db, sort_by, asc)

@app.put("/tournaments/{id}")
def update_tournament(id: int, tournament: schemas.Tournament_Update, db: Session = Depends(get_db)):
    try:
        crud.update_tournament(db, id, tournament)
        return "Tournament updated successfully"
    except Exception as e:
        raise HTTPException(400, f"Error updating tournament: {e}")

@app.delete("/tournaments/{id}")
def delete_tournament(id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_tournament(db, id)
        return "Tournament deleted successfully"
    except Exception as e:
        raise HTTPException(400, f"Error deleting tournament: {e}")


# partitipation--------------------------------------------------------------------

@app.post("/partitipations/")
def create_partitipation(partitipation: schemas.Partitipation_Create, db: Session = Depends(get_db)):
    try:
        crud.create_partitipation(db, partitipation)
        return "Partitipation created successfully"
    except Exception as e:
        raise HTTPException(400, f"Error creating partitipation: {e}")

@app.get("/partitipations/", response_model=list[schemas.Partitipation_Response])
def read_partitipations(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_partitipations(db, sort_by, asc)

@app.put("/partitipations/{id}")
def update_partitipation(id: int, partitipation: schemas.Partitipation_Update, db: Session = Depends(get_db)):
    try:
        crud.update_partitipation(db, id, partitipation)
        return "Partitipation updated successfully"
    except Exception as e:
        raise HTTPException(400, f"Error updating partitipation: {e}")

@app.delete("/partitipations/{id}")
def delete_partitipation(id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_partitipation(db, id)
        return "Partitipation deleted successfully"
    except Exception as e:
        raise HTTPException(400, f"Error deleting partitipation: {e}")

@app.get("/partitipation_results/", response_model=list[schemas.Results_response])
def read_partitipaiton_results(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_partitipation_results(db, sort_by, asc)

@app.put("/update_place/")
def update_place(initials: str, tournament: str, place:int, db: Session = Depends(get_db)):
    try:
        crud.update_place(db, initials, tournament, place)
        return "Place updated successfully"
    except Exception as e:
        raise HTTPException(400, f"Error updating place: {e}")

@app.get("/get_winners/", response_model=list[schemas.Winners_response])
def get_winners(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_winners(db, sort_by, asc)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)