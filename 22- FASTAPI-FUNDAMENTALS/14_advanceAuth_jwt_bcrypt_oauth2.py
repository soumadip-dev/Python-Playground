from datetime import datetime, timedelta, timezone

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()

# JWT configuration
JWT_SECRET = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing configuration
password_context = CryptContext(schemes=["bcrypt"])

# OAuth2 bearer token configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Mock user store (replace with a database in production)
users = {
    "admin": {
        "username": "admin",
        "hashed_password": password_context.hash("1234"),
    }
}


# Hash a plain-text password
def hash_password(password: str) -> str:
    return password_context.hash(password)


# Verify a plain-text password against a hashed password
def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return password_context.verify(
        plain_password,
        hashed_password,
    )


# Generate a JWT access token
def create_access_token(payload: dict) -> str:
    token_payload = payload.copy()

    expiration_time = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_payload.update(
        {
            "sub": payload["sub"],
            "exp": expiration_time,
        }
    )

    encoded_jwt = jwt.encode(
        token_payload,
        JWT_SECRET,
        algorithm=ALGORITHM,
    )

    return encoded_jwt


# Validate and decode a JWT access token
def verify_access_token(
    token: str = Depends(oauth2_scheme),
) -> str:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM],
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Invalid token payload.",
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token.",
        )


# Authenticate a user and generate an access token
@app.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user_record = users.get(form_data.username)

    if not user_record or not verify_password(
        form_data.password,
        user_record["hashed_password"],
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password.",
        )

    access_token = create_access_token(
        {
            "sub": form_data.username,
        }
    )

    return {
        "success": True,
        "message": "Login successful.",
        "data": {
            "access_token": access_token,
            "token_type": "bearer",
        },
    }


# Protected endpoint accessible only with a valid access token
@app.get("/protected")
def get_protected_resource(
    username: str = Depends(verify_access_token),
):
    return {
        "success": True,
        "message": "Authentication successful.",
        "data": {
            "username": username,
        },
    }
