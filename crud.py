from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

movies = [
    {
        "id": 100,
        "title": "Jurassic World",
        "platform": "Netflix",
        "date_released": "2015-06-12",
    },
    {
        "id": 101,
        "title": "Inception",
        "platform": "Amazon Prime",
        "date_released": "2010-07-16",
    },
    {
        "id": 102,
        "title": "The Dark Knight",
        "platform": "HBO Max",
        "date_released": "2008-07-18",
    },
    {
        "id": 103,
        "title": "Interstellar",
        "platform": "Paramount+",
        "date_released": "2014-11-07",
    },
]

app = FastAPI()


@app.get("/movie")
def get_movie():
    return movies


@app.get("/movie/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found")


class Movie(BaseModel):
    id: int
    title: str
    platform: str
    date_released: str


@app.post("/movie")
def create_movie(movie: Movie):
    new_movie = movie.model_dump()
    movies.append(new_movie)
    return new_movie


class MovieUpdate(BaseModel):
    title: str
    platform: str
    date_released: str


@app.put("/movie/{movie_id}")
def update_movie(movie_id: int, movie_update: MovieUpdate):
    for movie in movies:
        if movie["id"] == movie_id:
            movie["title"] = movie_update.title
            movie["platform"] = movie_update.platform
            movie["date_released"] = movie_update.date_released
            return movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found")


@app.delete("/movie/{movie_id}")
def delete_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return {"Message": "Movie has been deleted"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie Not Found")
