from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from envConfig import settings

DATABASE_URL = settings.DB_URI or ""

# Create the database engine
engine = create_engine(
    DATABASE_URL,
)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for all ORM models
Base = declarative_base()
