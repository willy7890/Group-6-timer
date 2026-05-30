from fastapi import APIRouter, HTTPException
from database import CLASSES, LEVEL_LABELS

router = APIRouter(tags=["Classes"])


@router.get("/levels/{level}/classes")
def get_classes(level: str):
    """Return all classes for a given education level."""
    if level not in LEVEL_LABELS:
        raise HTTPException(status_code=404, detail=f"Level '{level}' not found.")
    return CLASSES.get(level, [])
