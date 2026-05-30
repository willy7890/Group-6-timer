from fastapi import APIRouter, HTTPException
from database import SUBJECTS, LEVEL_LABELS

router = APIRouter(tags=["Subjects"])


@router.get("/levels/{level}/subjects")
def get_subjects(level: str):
    """Return all subjects for a given education level."""
    if level not in LEVEL_LABELS:
        raise HTTPException(status_code=404, detail=f"Level '{level}' not found.")
    return SUBJECTS.get(level, [])
