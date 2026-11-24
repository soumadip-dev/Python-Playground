from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, Header, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel

app = FastAPI()

JWT_SECRET = "secret_key"
ALGORITHM = "HS256"


# Generate JWT access token
def create_access_token(payload: dict) -> str:
    token_payload = payload.copy()

    expiration_time = datetime.now(timezone.utc) + timedelta(days=7)
    token_payload.update({"exp": expiration_time})

    encoded_jwt = jwt.encode(
        token_payload,
        JWT_SECRET,
        algorithm=ALGORITHM,
    )

    return encoded_jwt


# Verify JWT access token
def verify_access_token(token: str = Header(None)) -> str:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM],
        )

        username = payload.get("username")

        if not username:
            raise HTTPException(
                status_code=400,
                detail="Username not found in token payload.",
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token.",
        )


class User(BaseModel):
    username: str
    password: str


# Authenticate user and generate access token
@app.post("/login")
def login_user(user: User):
    if user.username != "admin" or user.password != "password":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password.",
        )

    access_token = create_access_token({"username": user.username})

    return {
        "success": True,
        "message": "Login successful.",
        "access_token": access_token,
    }


# Protected endpoint accessible only with a valid token
@app.get("/protected")
def get_protected_resource(
    username: str = Depends(verify_access_token),
):
    return {
        "success": True,
        "message": "Protected resource accessed successfully.",
        "username": username,
    }
