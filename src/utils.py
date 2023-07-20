from .statistics.logic import InteractionsRepository
from .database.database import get_session, Session
from typing import Union
from datetime import datetime
from .interface.logic import LinkRepository, LinkInterface
from .exceptions import AuthenticationFailed
from fastapi.security import APIKeyHeader
from fastapi import Depends, Path, Body
import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)


def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)


def get_link_id(link_id: str = Path(regex="^[A-Za-z0-9]{1,256}$")):
    return link_id


def get_original_link(original_link: str = Body(regex="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")):
    return original_link


def get_expiration_time(expiration_time: Union[None, str] = Body(regex="^(None|(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\\d\\d-([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d))$")):
    if expiration_time == "None":
        return None

    return datetime.strptime(expiration_time, "%d/%m/%Y-%H:%M:%S")

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

def get_interactions_repository(session: Session = Depends(get_session)):
    return InteractionsRepository(session)