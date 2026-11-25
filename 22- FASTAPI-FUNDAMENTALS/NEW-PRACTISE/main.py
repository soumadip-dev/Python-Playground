from fastapi import FastAPI
from routes import learn
from schemas.learn import MessageResponse

app = FastAPI()


app.include_router(learn.router)


@app.get("/", response_model=MessageResponse)
def root():
    return {"message": "Learning FastAPI"}
