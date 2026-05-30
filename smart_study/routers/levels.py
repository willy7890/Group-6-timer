from fastapi import APIRouter
from database import LEVEL_LABELS, LEVEL_COLORS

router = APIRouter(tags=["Levels"])


@router.get("/levels")
def get_levels():
    """Return all available education levels."""
    return [
        {
            "id":    level_id,
            "label": label,
            "color": LEVEL_COLORS[level_id],
        }
        for level_id, label in LEVEL_LABELS.items()
    ]
