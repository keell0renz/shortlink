from .logic import LinkRepository, LinkInterface
from fastapi import APIRouter, Depends, status
from ..database.database import get_session
from sqlalchemy.orm import Session
from typing import Union
from ..utils import (
    verify_api_key,
    get_link_id,
    get_link_interface,
    get_original_link,
    get_expiration_time
)

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/get/{link_id}", status_code=status.HTTP_200_OK, summary="(Deprecated)")
def api_get_link(
    link_id: str = Depends(get_link_id),
    interface: LinkInterface = Depends(get_link_interface)
):
    link_dict = interface.get_link_data(link_id)
    
    return link_dict

@router.post("/create/{link_id}", status_code=status.HTTP_201_CREATED, summary="(Deprecated)")
def api_create_link(
    link_id: str = Depends(get_link_id),
    original_link: str = Depends(get_original_link),
    expiration_time: Union[str, None] = Depends(get_expiration_time),
    interface: LinkInterface = Depends(get_link_interface)
):
    interface.create_link(link_id, original_link, expiration_time)

@router.delete("/delete/{link_id}", status_code=status.HTTP_201_CREATED, summary="(Deprecated)")
def api_delete_link(
    link_id: str = Depends(get_link_id),
    interface: LinkInterface = Depends(get_link_interface)
):
    interface.delete_link(link_id)

@router.put("/change/{link_id}/original_link", status_code=status.HTTP_201_CREATED, summary="(Deprecated)")
def api_change_original_link(
    link_id: str = Depends(get_link_id),
    new_original_link: str = Depends(get_original_link),
    interface: LinkInterface = Depends(get_link_interface)
):
    interface.change_original_link_by_link_id(link_id, new_original_link)

@router.put("/change/{link_id}/expiration_time", status_code=status.HTTP_201_CREATED, summary="(Deprecated)")
def api_change_expiration_time(
    link_id: str = Depends(get_link_id),
    new_expiration_time: Union[str, None] = Depends(get_expiration_time),
    interface: LinkInterface = Depends(get_link_interface)
):
    interface.change_expiration_time_by_link_id(link_id, new_expiration_time)

@router.delete("/delete/{link_id}/expiration_time", status_code=status.HTTP_201_CREATED, summary="(Deprecated)")
def api_delete_expiration_time(
    link_id: str = Depends(get_link_id),
    interface: LinkInterface = Depends(get_link_interface)
):
    interface.change_expiration_time_by_link_id(link_id, None)
