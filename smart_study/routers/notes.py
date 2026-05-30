from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import MY_DATABASE

router = APIRouter(tags=["Notes"])


# ── helpers ──────────────────────────────────────────────────────────────────

def _make_key(level: str, class_id: str, subject_id: str) -> str:
    return f"{level}__{class_id}__{subject_id}"


def _get_notes(level: str, class_id: str, subject_id: str) -> list[dict]:
    key = _make_key(level, class_id, subject_id)
    # Exact match
    if key in MY_DATABASE:
        return MY_DATABASE[key]
    # Case-insensitive fallback
    lower = key.lower()
    for k, v in MY_DATABASE.items():
        if k.lower() == lower:
            return v
    return []


# ── schemas ──────────────────────────────────────────────────────────────────

class NoteIn(BaseModel):
    title: str
    body: Optional[str] = ""
    body_html: Optional[str] = None
    note_type: Optional[str] = None   # "interactive" or None


# ── routes ───────────────────────────────────────────────────────────────────

@router.get("/levels/{level}/classes/{class_id}/subjects/{subject_id}/notes")
def list_notes(level: str, class_id: str, subject_id: str):
    """List all notes (title only) for a subject."""
    notes = _get_notes(level, class_id, subject_id)
    return [{"index": i, "title": n["title"]} for i, n in enumerate(notes)]


@router.get("/levels/{level}/classes/{class_id}/subjects/{subject_id}/notes/{index}")
def get_note(level: str, class_id: str, subject_id: str, index: int):
    """Return a single note by index."""
    notes = _get_notes(level, class_id, subject_id)
    if index < 0 or index >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found.")
    return notes[index]


@router.post("/levels/{level}/classes/{class_id}/subjects/{subject_id}/notes",
             status_code=201)
def add_note(level: str, class_id: str, subject_id: str, note: NoteIn):
    """
    Add a new note to a subject.
    This is how you write new book chapters into the database at runtime.
    The note is kept in memory until the server restarts.
    Persist to database.py manually for permanent storage.
    """
    key = _make_key(level, class_id, subject_id)
    if key not in MY_DATABASE:
        MY_DATABASE[key] = []

    new_note: dict = {"title": note.title, "body": note.body or ""}
    if note.body_html:
        new_note["body_html"] = note.body_html
    if note.note_type:
        new_note["type"] = note.note_type

    MY_DATABASE[key].append(new_note)
    return {"message": "Note added successfully.", "index": len(MY_DATABASE[key]) - 1}


@router.put("/levels/{level}/classes/{class_id}/subjects/{subject_id}/notes/{index}")
def update_note(level: str, class_id: str, subject_id: str, index: int, note: NoteIn):
    """Update an existing note by index."""
    notes = _get_notes(level, class_id, subject_id)
    if index < 0 or index >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found.")

    key = _make_key(level, class_id, subject_id)
    updated: dict = {"title": note.title, "body": note.body or ""}
    if note.body_html:
        updated["body_html"] = note.body_html
    if note.note_type:
        updated["type"] = note.note_type

    MY_DATABASE[key][index] = updated
    return {"message": "Note updated successfully."}


@router.delete("/levels/{level}/classes/{class_id}/subjects/{subject_id}/notes/{index}")
def delete_note(level: str, class_id: str, subject_id: str, index: int):
    """Delete a note by index."""
    notes = _get_notes(level, class_id, subject_id)
    if index < 0 or index >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found.")

    key = _make_key(level, class_id, subject_id)
    MY_DATABASE[key].pop(index)
    return {"message": "Note deleted successfully."}
