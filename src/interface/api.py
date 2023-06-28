from fastapi import APIRouter, Path, Body, Depends

from ..utils import verify_api_key, get_link_id, get_original_link, get_expiration_time

from typing import Union

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/get/{link_id}")
async def api_get_link(link_id: str = Depends(get_link_id)):
    pass


@router.post("/create/{link_id}")
async def api_create_link(link_id: str = Depends(get_link_id), original_link: str = Depends(get_original_link), expiration_time: Union[str, None] = Depends(get_expiration_time)):
    pass


@router.delete("/delete/{link_id}")
async def api_delete_link(link_id: str = Depends(get_link_id)):
    pass


@router.put("/change/{link_id}/original_link")
async def api_change_original_link(link_id: str = Depends(get_link_id), new_original_link: str = Depends(get_original_link)):
    pass


@router.put("/change/{link_id}/expiration_time")
async def api_change_expiration_date(link_id: str = Depends(get_link_id), new_expiration_time: Union[str, None] = Depends(get_expiration_time)):
    pass


@router.delete("/delete/{link_id}/expiration_time")
async def api_delete_expiration_date(link_id: str = Depends(get_link_id)):
    pass
