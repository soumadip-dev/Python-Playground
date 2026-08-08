from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My first FastAPI server is running ✅"}


@app.get("/about")
def about():
    return {"project": "loan risk model", "version": "0.1"}
