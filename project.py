from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import session
import model
from pydantic import BaseModel

app = FastAPI()


class MovieCollection(BaseModel):
    id: int
    title: str
    platform: str
    date_released: str


@app.post("/movies")
def create_movie(movie: MovieCollection, db: session = Depends(get_db)):
    new_movie = model.Movie(
        id=movie.id,
        title=movie.title,
        platform=movie.platform,
        date_released=movie.date_released,
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


@app.get("/movies")
def get_movie(db: session = Depends(get_db)):
    movies = db.query(model.Movie).all()
    return movies
