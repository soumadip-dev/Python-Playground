import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_URI = os.getenv("DB_URL")

    ORIGINS: list[str] = os.getenv(
        "ORIGINS",
        "",
    ).split(",")

    APP_NAME: str = os.getenv("APP_NAME") or "FastAPI"

    APP_VERSION: str = os.getenv("APP_VERSION") or "1.0.0"

    JWT_SECRET: str = os.getenv("JWT_SECRET") or "secret"


settings = Settings()
