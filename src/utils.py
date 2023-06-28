from fastapi import Depends
from fastapi.security import APIKeyHeader

from .exceptions import AuthenticationFailed

import os

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("SHORTLINK_API_KEY"):
        raise AuthenticationFailed(api_key)