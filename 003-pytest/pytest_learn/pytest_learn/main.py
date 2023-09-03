# This code is written very simple (and kinda dirty)

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = "sqlite:///./test.db"
Base: DeclarativeMeta = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI()


class AnimalCreate(BaseModel):
    name: str
    species: str
    age: int


@app.post("/add_animal/", response_model=AnimalCreate)
def add_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    db_animal = Animal(**animal.model_dump())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


@app.get("/animals/", response_model=list[AnimalCreate])
def read_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Animal).offset(skip).limit(limit).all()
