from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from envConfig import settings

# JWT configuration
JWT_SECRET = settings.JWT_SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Password hashing configuration
password_context = CryptContext(schemes=["bcrypt"])

# OAuth2 bearer token configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Hash a plain-text password
def hash_password(password: str) -> str:
    return password_context.hash(password)


# Generate a JWT access token
def create_access_token(payload: dict) -> str:
    token_payload = payload.copy()

    expiration_time = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_payload.update(
        {
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
):
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM],
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token.",
        )
