import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    SECRET_KEY: str | None = os.getenv("SECRET_KEY")

    ORIGINS: list[str] = os.getenv("ORIGINS", "").split(",")

    DB_URL: str | None = os.getenv("DB_URL")

    APP_NAME: str = (
        os.getenv(
            "APP_NAME",
        )
        or "FastAPI"
    )

    APP_VERSION: str = (
        os.getenv(
            "APP_VERSION",
        )
        or "1.0.0"
    )


settings = Settings()
