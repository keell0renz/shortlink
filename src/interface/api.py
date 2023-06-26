from fastapi import APIRouter, Path, Body, Depends
from fastapi.security import APIKeyHeader

from ..exceptions import AuthenticationFailed

from typing import Union
import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/get/{link_id}")
async def api_get_link(link_id: str = Path(...)):
    pass


@router.post("/create/{link_id}")
async def api_create_link(link_id: str = Path(...), original_link: str = Body(...), expiration_time: Union[str, None] = Body(...)):
    pass


@router.delete("/delete/{link_id}")
async def api_delete_link(link_id: str = Path(...)):
    pass


@router.put("/change/{link_id}/original_link")
async def api_change_original_link(link_id: str = Path(...), new_original_link: str = Body(...)):
    pass


@router.put("/change/{link_id}/expiration_time")
async def api_change_expiration_date(link_id: str = Path(...), new_expiration_time: Union[str, None] = Body(...)):
    pass


@router.delete("/delete/{link_id}/expiration_time")
async def api_delete_expiration_date(link_id: str = Path(...)):
    pass
