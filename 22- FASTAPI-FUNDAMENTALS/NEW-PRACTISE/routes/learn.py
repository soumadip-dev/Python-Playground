from fastapi import APIRouter, HTTPException
from schemas.learn import (
    NoteUpdate,
    NoteCreate,
    NoteResponse,
    NotesResponse,
)
from data.notes import notes

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/terms", response_model=NotesResponse)
def get_terms(tag: str | None = None, q: str | None = None):
    # Query parameters

    result = []
    for note in notes:
        if tag and tag not in note["tags"]:
            continue
        if q and q.lower() not in note["term"].lower():
            continue
        result.append(note)

    return {"message": "Notes fetched successfully", "data": result}


# path parameter
@router.get("/terms/{term_id}", response_model=NoteResponse)
def get_term_by_id(term_id: int):
    for note in notes:
        if note["id"] == term_id:
            return {"message": "Note fetched successfully", "data": note}

    raise HTTPException(status_code=404, detail="Note not found")


@router.post("/terms", response_model=NoteResponse, status_code=201)
def add_term(note: NoteCreate):
    for existing in notes:
        if existing["term"].lower() == note.term.lower():
            raise HTTPException(status_code=400, detail="Term already exists")

    new_note = {"id": len(notes) + 1}

    # model_dump() returns a dictionary representation of the Pydantic model instance, which can be used to update the new_note dictionary with the fields from the NoteCreate model.
    new_note.update(note.model_dump())

    notes.append(new_note)

    return {"message": "New note added successfully", "data": new_note}


@router.patch("/terms/{term_id}", response_model=NoteResponse)
def update_term(term_id: int, changes: NoteUpdate):
    for note in notes:
        if note["id"] == term_id:
            # If we dont send the exclude_unset=True, it will overwrite the existing values with None if they are not provided in the request body.
            note.update(changes.model_dump(exclude_unset=True))

            return {"message": "Note updated successfully", "data": note}

    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/terms/{term_id}", status_code=204)
def delete_term(term_id: int):
    for note in notes:
        if note["id"] == term_id:
            notes.remove(note)
            return
    raise HTTPException(status_code=404, detail="Note not found")
