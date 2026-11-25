from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    genre: List[str]


class MovieResponse(BaseModel):
    message: str
    data: Movie


class MoviesResponse(BaseModel):
    message: str
    data: List[Movie]


class MessageResponse(BaseModel):
    message: str


class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    genre: List[str]


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None
    genre: List[str] | None = None
