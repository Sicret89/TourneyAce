import os
from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")  # Default SQLite

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    print("Initializing the database...")
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
   with Session(engine) as session:
       yield session
