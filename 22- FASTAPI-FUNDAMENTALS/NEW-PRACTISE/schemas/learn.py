from pydantic import BaseModel
from typing import List


class Note(BaseModel):
    id: int
    term: str
    definition: str
    tags: List[str]


class NoteResponse(BaseModel):
    message: str
    data: Note


class NotesResponse(BaseModel):
    message: str
    data: List[Note]


class MessageResponse(BaseModel):
    message: str


class NoteCreate(BaseModel):
    term: str
    definition: str
    tags: List[str]


class NoteUpdate(BaseModel):
    term: str | None = None
    definition: str | None = None
    tags: List[str] | None = None
