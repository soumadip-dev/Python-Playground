from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Full model (contains sensitive data)
class User(BaseModel):
    username: str
    email: str
    password: str


# Response model (hides password)
class UserResponse(BaseModel):
    username: str
    email: str


@app.get("/user", response_model=UserResponse)
def get_user():
    return User(
        username="john_doe",
        email="john@example.com",
        password="secret123",  # This won't be returned
    )
