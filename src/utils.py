from fastapi import Depends, Path, Body
from fastapi.security import APIKeyHeader
from .exceptions import AuthenticationFailed
from typing import Union
from datetime import datetime
import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)


async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)


async def get_link_id(link_id: str = Path(regex="^[A-Za-z0-9]{1,256}$")):
    return link_id


async def get_original_link(original_link: str = Body(regex="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")):
    return original_link


async def get_expiration_time(expiration_time: Union[None, str] = Body(regex="^(None|(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\\d\\d-([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d))$")):
    if expiration_time == "None":
        return None

    return datetime.strptime(expiration_time, "%d/%m/%Y-%H:%M:%S")
