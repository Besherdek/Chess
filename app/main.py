from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

app = FastAPI()

@app.post("/chess_players/", response_model=schemas.Chess_Player_Create)
def create_chess_player(chess_player: schemas.Chess_Player_Create, db: Session = Depends(get_db)):
    return crud.create_chess_player(db, chess_player)

@app.post("/tournaments/", response_model=schemas.Tournament_Create)
def create_tournament(tournament: schemas.Tournament_Create, db: Session = Depends(get_db)):
    return crud.create_tournament(db, tournament)

@app.post("/partitipations/", response_model=schemas.Partitipation_Create)
def create_partitipation(partitipation: schemas.Partitipation_Create, db: Session = Depends(get_db)):
    return crud.create_partitipation(db, partitipation)


@app.get("/chess_players/", response_model=list[schemas.Chess_Player_Response])
def read_chess_players(db: Session = Depends(get_db)):
    return crud.read_chess_players(db)

@app.get("/tournaments/", response_model=list[schemas.Tournament_Response])
def read_tournaments(db: Session = Depends(get_db)):
    return crud.read_tournaments(db)

@app.get("/partitipations/", response_model=list[schemas.Partitipation_Response])
def read_partitipations(db: Session = Depends(get_db)):
    return crud.read_partitipations(db)


@app.put("/chess_players/{id}", response_model=schemas.Chess_Player_Response)
def update_chess_player(id: int, chess_player: schemas.Chess_Player_Update, db: Session = Depends(get_db)):
    updated_chess_player = crud.update_chess_player(db, id, chess_player)

    if not updated_chess_player:
        raise HTTPException(404, "Error: chess player with such id not found")
    return updated_chess_player

@app.put("/tournaments/{id}", response_model=schemas.Tournament_Response)
def update_tournament(id: int, tournament: schemas.Tournament_Update, db: Session = Depends(get_db)):
    updated_tournament = crud.update_tournament(db, id, tournament)

    if not updated_tournament:
        raise HTTPException(404, "Error: tournament with such id not found")
    return updated_tournament

@app.put("/partitipation/{id}", response_model=schemas.Partitipation_Response)
def update_partitipation(id: int, partitipation: schemas.Partitipation_Update, db: Session = Depends(get_db)):
    updated_partitipation = crud.update_partitipation(db, id, partitipation)

    if not updated_partitipation:
        raise HTTPException(404, "Error: partitipation with such id not found")
    return updated_partitipation


@app.delete("/chess_players/{id}", response_model=dict)
def delete_chess_player(id: int, db: Session = Depends(get_db)):
    success = crud.delete_chess_player(db, id)
    if not success:
        raise HTTPException(404, "Error: chess player with such id not found")
    return {"Detail": "Chess player deleted successfully"}

@app.delete("/tournaments/{id}", response_model=dict)
def delete_tournament(id: int, db: Session = Depends(get_db)):
    success = crud.delete_tournament(db, id)
    if not success:
        raise HTTPException(404, "Error: tournament with such id not found")
    return {"Detail": "Tournament deleted successfully"}

@app.delete("/partitipation/{id}", response_model=dict)
def delete_partitipation(id: int, db: Session = Depends(get_db)):
    success = crud.delete_partitipation(db, id)
    if not success:
        raise HTTPException(404, "Error: partitipation with such id not found")
    return {"Detail": "Partitipation deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)