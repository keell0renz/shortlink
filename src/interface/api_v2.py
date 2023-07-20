from fastapi import APIRouter, Depends, status
from typing import Union
from sqlalchemy.orm import Session
from ..database.database import get_session
from ..utils import (
    verify_api_key,
    get_link_id,
    get_original_link,
    get_expiration_time
)
from .logic import LinkRepository, LinkInterface
from fastapi_utils import cbv
from pydantic import BaseModel

def get_link_repository(session: Session = Depends(get_session)):
    return LinkRepository(session)

def get_link_interface(repository: LinkRepository = Depends(get_link_repository)):
    return LinkInterface(repository)

router = APIRouter(dependencies=[Depends(verify_api_key)])

from fastapi import APIRouter, Depends, status
from typing import Union
from sqlalchemy.orm import Session
from ..database.database import get_session
from ..utils import (
    verify_api_key,
    get_link_id,
    get_original_link,
    get_expiration_time
)
from .logic import LinkRepository, LinkInterface
from fastapi_utils.cbv import cbv
from pydantic import BaseModel

def get_link_repository(session: Session = Depends(get_session)):
    return LinkRepository(session)

def get_link_interface(repository: LinkRepository = Depends(get_link_repository)):
    return LinkInterface(repository)

def get_link_data(
        original_link = Depends(get_original_link),
        expiration_time = Depends(get_expiration_time)
):
    return {
        "original_link": original_link,
        "expiration_time": expiration_time
    }

router = APIRouter(dependencies=[Depends(verify_api_key)])

@cbv(router)
class LinkAPI:
    interface: LinkInterface = Depends(get_link_interface)
    
    @router.get("/get/{link_id}", status_code=status.HTTP_200_OK)
    def api_get_link(self, link_id: str = Depends(get_link_id)):
        link_dict = self.interface.get_link_data(link_id)
        
        return link_dict
    
    @router.post("/create/{link_id}", status_code=status.HTTP_201_CREATED)
    def api_create_link(self, link_id: str = Depends(get_link_id), link_data: dict = Depends(get_link_data)):
        self.interface.create_link(link_id, link_data["original_link"], link_data["expiration_time"])

    @router.put("/change/{link_id}", status_code=status.HTTP_201_CREATED)
    def api_change_link(self, link_id: str = Depends(get_link_id), link_data: dict = Depends(get_link_data)):
        self.interface.change_original_link_by_link_id(link_id, link_data["original_link"])
        self.interface.change_expiration_time_by_link_id(link_id, link_data["expiration_time"])
