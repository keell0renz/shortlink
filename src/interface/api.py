from fastapi import APIRouter, Path, Body, Depends
from typing import Union

router = APIRouter()

@router.get("/get/{link_id}")
async def api_get_link(link_id: str = Path(...)):
    pass


@router.post("/create/{link_id}")
async def api_create_link(link_id: str = Path(...), original_link: str = Body(...), expires: Union[str, None] = Body(...)):
    pass


@router.delete("/delete/{link_id}")
async def api_delete_link(link_id: str = Path(...)):
    pass


@router.put("/change/{link_id}/original_link")
async def api_change_original_link(link_id: str = Path(...), new_original_link: str = Body(...)):
    pass


@router.put("/change/{link_id}/expiration_date")
async def api_change_expiration_date(link_id: str = Path(...), new_expiration_date: Union[str, None] = Body(...)):
    pass


@router.delete("/delete/{link_id}/expiration_date")
async def api_delete_expiration_date(link_id: str = Path(...)):
    pass
