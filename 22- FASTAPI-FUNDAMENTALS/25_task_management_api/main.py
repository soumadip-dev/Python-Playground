from fastapi import FastAPI

from src.utils.db import Base, engine
from src.tasks.models import TaskModel
from src.tasks.router import task_routes

tags_metadata = [
    {
        "name": "Tasks",
        "description": "Create, update, and delete tasks.",
    },
    {
        "name": "Users",
        "description": "Manage user accounts.",
    },
]


app = FastAPI(
    title="Task Management Application",
    summary="A lightweight REST API for organizing daily tasks.",
    description="Manage tasks with **priorities**, **deadlines**, and **status tracking**.",
    version="1.0.0",
    contact={
        "name": "Soumadip Majila",
        "email": "soumadipmajila@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=tags_metadata,
)


app.include_router(task_routes)


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
