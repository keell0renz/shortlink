from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from ..utils import get_link_id
from sqlalchemy.orm import Session
from ..database.database import get_session
from .logic import LinkRepository, LinkInterface


def get_link_repository(session: Session = Depends(get_session)):
    return LinkRepository(session)


def get_link_interface(repository: LinkRepository = Depends(get_link_repository)):
    return LinkInterface(repository)

router = APIRouter()


@router.get("/{link_id}")
def ui_get_link(request: Request, link_id: str = Depends(get_link_id), interface: LinkInterface = Depends(get_link_interface)):
    original_link = interface.get_original_link_by_link_id(link_id)
    interface.add_interaction(
        link_id,
        request.client.host,
        None,
        request.headers.get("User-Agent"))

    return RedirectResponse(
        url=original_link
    )
