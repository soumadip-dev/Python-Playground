from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskResponseSchema, APIResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/task", tags=["Tasks"])


@task_routes.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=APIResponseSchema[TaskResponseSchema],
)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


@task_routes.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=APIResponseSchema[list[TaskResponseSchema]],
)
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)


@task_routes.get(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=APIResponseSchema[TaskResponseSchema],
)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    return controller.get_task_by_id(task_id, db)


@task_routes.put(
    "/{task_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=APIResponseSchema[TaskResponseSchema],
)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)


@task_routes.delete(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=APIResponseSchema[None],
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)
