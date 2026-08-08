from typing import List
from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogData(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


class BlogResponse(BaseModel):
    success: bool
    message: str
    data: BlogData


class BlogListResponse(BaseModel):
    success: bool
    message: str
    page: int
    limit: int
    data: List[BlogData]


class LoginResponse(BaseModel):
    success: bool
    message: str
    access_token: str
    token_type: str
