from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from .models import Base

url = URL.create (
    drivername="postgresql",
    username="diddy",
    password="",
    host="localhost",
    database="chessdb",
    port=5432
)

engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)