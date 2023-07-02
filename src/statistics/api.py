from fastapi import APIRouter, Path, Depends
from ..utils import verify_api_key, get_link_id

from sqlalchemy.orm import Session
from ..database.database import get_session
from .logic import InteractionsRepository

async def get_interactions_repository(session: Session = Depends(get_session)):
    return InteractionsRepository(session)

router = APIRouter(dependencies=[Depends(verify_api_key)])

@router.get("/links")
async def stat_api_get_all_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    pass

@router.get("/active_links")
async def stat_api_get_active_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    pass

@router.get("/expired_links")
async def stat_api_get_expired_links(repository: InteractionsRepository = Depends(get_interactions_repository)):
    pass

@router.get("/interactions/{link_id}")
async def stat_api_get_link_interactions(link_id: str = Depends(get_link_id), repository: InteractionsRepository = Depends(get_interactions_repository)):
    pass
