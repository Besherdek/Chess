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

@app.post("/chess_players/", response_model=schemas.Chess_Player_Create)
def create_chess_player(chess_player: schemas.Chess_Player_Create, db: Session = Depends(get_db)):
    return crud.create_chess_player(db, chess_player)

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

@app.put("/chess_players/{id}", response_model=schemas.Chess_Player_Response)
def update_chess_player(id: int, chess_player: schemas.Chess_Player_Update, db: Session = Depends(get_db)):
    updated_chess_player = crud.update_chess_player(db, id, chess_player)

    if not updated_chess_player:
        raise HTTPException(404, "Error: chess player with such id not found")
    return updated_chess_player

@app.delete("/chess_players/{id}", response_model=dict)
def delete_chess_player(id: int, db: Session = Depends(get_db)):
    success = crud.delete_chess_player(db, id)
    if not success:
        raise HTTPException(404, "Error: chess player with such id not found")
    return {"Detail": "Chess player deleted successfully"}


# tournament--------------------------------------------------------------------

@app.post("/tournaments/", response_model=schemas.Tournament_Create)
def create_tournament(tournament: schemas.Tournament_Create, db: Session = Depends(get_db)):
    return crud.create_tournament(db, tournament)

@app.get("/tournaments/", response_model=list[schemas.Tournament_Response])
def read_tournaments(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_tournaments(db, sort_by, asc)

@app.put("/tournaments/{id}", response_model=schemas.Tournament_Response)
def update_tournament(id: int, tournament: schemas.Tournament_Update, db: Session = Depends(get_db)):
    updated_tournament = crud.update_tournament(db, id, tournament)

    if not updated_tournament:
        raise HTTPException(404, "Error: tournament with such id not found")
    return updated_tournament

@app.delete("/tournaments/{id}", response_model=dict)
def delete_tournament(id: int, db: Session = Depends(get_db)):
    success = crud.delete_tournament(db, id)
    if not success:
        raise HTTPException(404, "Error: tournament with such id not found")
    return {"Detail": "Tournament deleted successfully"}


# partitipation--------------------------------------------------------------------

@app.post("/partitipations/", response_model=schemas.Partitipation_Create)
def create_partitipation(partitipation: schemas.Partitipation_Create, db: Session = Depends(get_db)):
    return crud.create_partitipation(db, partitipation)

@app.get("/partitipations/", response_model=list[schemas.Partitipation_Response])
def read_partitipations(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_partitipations(db, sort_by, asc)

@app.put("/partitipations/{id}", response_model=schemas.Partitipation_Response)
def update_partitipation(id: int, partitipation: schemas.Partitipation_Update, db: Session = Depends(get_db)):
    updated_partitipation = crud.update_partitipation(db, id, partitipation)

    if not updated_partitipation:
        raise HTTPException(404, "Error: partitipation with such id not found")
    return updated_partitipation

@app.delete("/partitipations/{id}", response_model=dict)
def delete_partitipation(id: int, db: Session = Depends(get_db)):
    success = crud.delete_partitipation(db, id)
    if not success:
        raise HTTPException(404, "Error: partitipation with such id not found")
    return {"Detail": "Partitipation deleted successfully"}

@app.get("/partitipation_results/", response_model=list[schemas.Results_response])
def read_partitipaiton_results(
    sort_by: str = None,
    asc: bool = True,
    db: Session = Depends(get_db)
    ):
    return crud.read_partitipation_results(db, sort_by, asc)

@app.put("/update_place/")
def update_place(initials: str, tournament: str, place:int, db: Session = Depends(get_db)):
    crud.update_place(db, initials, tournament, place)

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