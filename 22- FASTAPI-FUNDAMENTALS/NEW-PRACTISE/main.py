from fastapi import FastAPI
from routes import movie
from schemas.movie import MessageResponse

app = FastAPI()


app.include_router(movie.router)


@app.get("/", response_model=MessageResponse)
def root():
    return {"message": "Learning FastAPI"}
