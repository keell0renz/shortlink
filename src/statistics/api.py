from sqlalchemy.orm import Session
from fastapi import Depends, status
from fastapi import APIRouter
from ..database.database import get_session
from ..utils import (
    get_interactions_repository,
    get_link_id,
    verify_api_key,
    InteractionsRepository,
)

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/links", status_code=status.HTTP_200_OK)
def stat_api_get_all_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    return repository.get_all_link_records()

@router.get("/active_links", status_code=status.HTTP_200_OK)
def stat_api_get_active_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    return repository.get_all_active_links()

@router.get("/expired_links", status_code=status.HTTP_200_OK)
def stat_api_get_expired_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    return repository.get_all_expired_links()

@router.get("/interactions/{link_id}", status_code=status.HTTP_200_OK)
def stat_api_get_link_interactions(
    link_id: str = Depends(get_link_id),
    repository: InteractionsRepository = Depends(get_interactions_repository)
):
    return repository.get_link_interactions_by_link_id(link_id)
