from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException


def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        "message": "Task created successfully",
        "data": new_task,
    }


def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()

    return {
        "message": "Tasks retrieved successfully",
        "data": tasks,
    }


def get_task_by_id(task_id: int, db: Session):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return {
        "message": "Task retrieved successfully",
        "data": task,
    }


def update_task(body: TaskSchema, task_id: int, db: Session):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    changes = body.model_dump(exclude_unset=True)

    for key, value in changes.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return {
        "message": "Task updated successfully",
        "data": task,
    }


def delete_task(task_id: int, db: Session):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully",
        "data": None,
    }
