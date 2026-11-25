from fastapi import APIRouter, HTTPException

from schemas.movie import (
    MovieCreate,
    MovieUpdate,
    MovieResponse,
    MoviesResponse,
)

from data.movies import movies

router = APIRouter(prefix="/movies", tags=["movies"])


# Query parameters
@router.get("/", response_model=MoviesResponse)
def get_movies(genre: str | None = None, q: str | None = None):

    result = []

    for movie in movies:
        if genre and genre not in movie["genre"]:
            continue

        if q and q.lower() not in movie["title"].lower():
            continue

        result.append(movie)

    return {
        "message": "Movies fetched successfully",
        "data": result,
    }


# Path parameter
@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie_by_id(movie_id: int):

    for movie in movies:
        if movie["id"] == movie_id:
            return {
                "message": "Movie fetched successfully",
                "data": movie,
            }

    raise HTTPException(status_code=404, detail="Movie not found")


# POST - Create a new movie
@router.post("/", response_model=MovieResponse, status_code=201)
def add_movie(movie: MovieCreate):

    for existing in movies:
        if existing["title"].lower() == movie.title.lower():
            raise HTTPException(
                status_code=400,
                detail="Movie already exists",
            )

    new_movie = {"id": len(movies) + 1}

    new_movie.update(movie.model_dump())

    movies.append(new_movie)

    return {
        "message": "New movie added successfully",
        "data": new_movie,
    }


# PATCH - Partially update a movie
@router.patch("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, changes: MovieUpdate):

    for movie in movies:
        if movie["id"] == movie_id:

            movie.update(changes.model_dump(exclude_unset=True))

            return {
                "message": "Movie updated successfully",
                "data": movie,
            }

    raise HTTPException(status_code=404, detail="Movie not found")


# PUT - Replace a movie
@router.put("/{movie_id}", response_model=MovieResponse)
def replace_movie(movie_id: int, updated_movie: MovieCreate):

    for movie in movies:
        if movie["id"] == movie_id:

            movie.update(updated_movie.model_dump())

            return {
                "message": "Movie replaced successfully",
                "data": movie,
            }

    raise HTTPException(status_code=404, detail="Movie not found")


# DELETE - Delete a movie
@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int):

    for movie in movies:
        if movie["id"] == movie_id:

            movies.remove(movie)

            return

    raise HTTPException(status_code=404, detail="Movie not found")
