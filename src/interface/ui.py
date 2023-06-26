from fastapi import APIRouter, Path

router = APIRouter()

@router.get("/{link_id}")
async def ui_get_link(link_id: str = Path()):
    pass