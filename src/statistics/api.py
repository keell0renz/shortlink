from fastapi import APIRouter, Path, Depends
from ..utils import verify_api_key, get_link_id

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/link/{link_id}")
async def stat_api_get_link_statistics(link_id: str = Depends(get_link_id)):
    pass

@router.get("/links")
async def stat_api_get_all_links():
    pass


@router.get("/active_links")
async def stat_api_get_active_links():
    pass


@router.get("/expired_links")
async def stat_api_get_expired_links():
    pass

@router.get("/interactions/{link_id}")
async def stat_api_get_link_interactions(link_id: str = Depends(get_link_id)):
    pass
