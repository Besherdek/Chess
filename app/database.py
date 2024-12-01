from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from models import Base

url = URL.create (
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="chessdb",
    port=5432
)

engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)