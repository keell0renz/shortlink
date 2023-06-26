from fastapi import APIRouter, Path, Depends
from fastapi.security import APIKeyHeader

from ..exceptions import AuthenticationFailed

import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/link/{link_id}")
async def stat_api_get_link_statistics(link_id: str = Path(...)):
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
async def stat_api_get_link_interactions(link_id: str = Path(...)):
    pass
