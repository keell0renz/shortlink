from fastapi import APIRouter, Path, Depends

from ..utils import get_link_id

router = APIRouter()

@router.get("/{link_id}")
async def ui_get_link(link_id: str = Depends(get_link_id)):
    pass