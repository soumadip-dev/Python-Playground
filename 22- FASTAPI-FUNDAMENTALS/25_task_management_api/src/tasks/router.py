from fastapi import APIRouter
from src.tasks import controller

task_routes = APIRouter(prefix="/task", tags=["Tasks"])


@task_routes.post("/create")
def create_task():
    return controller.create_task()
