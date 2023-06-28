from fastapi import Depends, Path, Body
from fastapi.security import APIKeyHeader

from .exceptions import AuthenticationFailed

from typing import Union
import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)
    
async def get_link_id(link_id: str = Path(...)):
    return link_id

async def get_original_link(original_link: str = Body(...)):
    return original_link

async def get_expiration_time(expiration_time: Union[None, str] = Body(...)):
    return expiration_time