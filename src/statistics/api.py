from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..utils import verify_api_key, get_link_id, get_interactions_repository, InteractionsRepository
from ..database.database import get_session

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
