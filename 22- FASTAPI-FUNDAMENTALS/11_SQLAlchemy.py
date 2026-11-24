from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

# Initialize FastAPI application
app = FastAPI(
    title="Todo API",
    version="1.0.0",
    description="A simple CRUD API for managing todo items using FastAPI and SQLite.",
)


# SQLite database URL
DATABASE_URL = "sqlite:///./test.db"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Required for SQLite with FastAPI
)


# Create a configured "SessionLocal" class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


# Database model for Todo items
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(String, default="false")


# Create all tables in the database
Base.metadata.create_all(bind=engine)


def get_db():
    """
    Dependency that provides a database session.
    Ensures the session is closed after request completion.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root(db: Session = Depends(get_db)):
    return {
        "status": "success",
        "message": "FastAPI application is running and SQLite database is connected successfully.",
    }


# Create a new Todo item
@app.post("/todos")
def create_todo(title: str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed="false")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "status": "success",
        "message": f"Todo item created successfully.",
        "data": todo,
    }


# Get all Todo items
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {
        "status": "success",
        "message": "Todo items retrieved successfully.",
        "data": todos,
    }


# Get a specific Todo item by ID
@app.get("/todos/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {
        "status": "success",
        "message": "Todo item retrieved successfully.",
        "data": todo,
    }


# Update a Todo item by ID
@app.put("/todos/{id}")
def update_todo(id: int, title: str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    todo.title = title  # type: ignore
    db.commit()
    db.refresh(todo)

    return {
        "status": "success",
        "message": f"Todo item updated successfully.",
        "data": todo,
    }


# Delete a Todo item by ID
@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    db.delete(todo)
    db.commit()

    return {
        "status": "success",
        "message": f"Todo item deleted successfully.",
    }


# Delete all Todo items
@app.delete("/todos")
def delete_all_todos(db: Session = Depends(get_db)):
    db.query(Todo).delete()
    db.commit()

    return {
        "status": "success",
        "message": "All Todo items deleted successfully.",
    }
