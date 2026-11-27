from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class APIResponseSchema(BaseModel, Generic[T]):
    message: str
    data: T | None = None


class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool = False
