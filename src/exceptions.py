from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class AuthenticationFailed(Exception):
    def __init__(self, api_key):
        self.api_key = api_key

    def response(self):
        return JSONResponse(
            status_code=403,
            content={
                "exception": "Authentication failed.",
                "detail": f"API Key: {self.api_key} is not valid."
            }
        )

class LinkAlreadyExists(Exception):
    def __init__(self, link_id):
        self.link_id = link_id

    def response(self):
        return JSONResponse(
            status_code=403,
            content={
                "exception": "Link already exists.",
                "detail": f"Link ID: {self.link_id} cannot be used, as it is already in use."
            }
        )

class LinkDoesNotExist(Exception):
    def __init__(self, link_id):
        self.link_id = link_id

    def response(self):
        return JSONResponse(
            status_code=404,
            content={
                "exception": "Link does not exist.",
                "detail": f"Link ID: {self.link_id} cannot be used, because is does not exist."
            }
        )
    
class LinkHasExpired(Exception):
    def __init__(self, link_id):
        self.link_id = link_id

    def response(self):
        return JSONResponse(
            status_code=404,
            content={
                "exception": "Link has expired!",
                "detail": f"Link ID: {self.link_id} cannot be used, becuase it has expired."
            }
        )
    
class InternalSQLAlchemyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def response(self):
        return JSONResponse(
            status_code=503,
            content={
                "exception": "Some SQLAlchemy internal error (not integrity error).",
                "detail": f"{self.msg}"
            }
        )
    
@app.exception_handler(AuthenticationFailed)
async def exception_authentication_failed(request: Request, exception: AuthenticationFailed):
    return exception.response()

@app.exception_handler(LinkAlreadyExists)
async def exception_link_already_exists(request: Request, exception: LinkAlreadyExists):
    return exception.response()

@app.exception_handler(LinkDoesNotExist)
async def exception_link_does_not_exist(request: Request, exception: LinkDoesNotExist):
    return exception.response()

@app.exception_handler(LinkHasExpired)
async def exception_link_has_expired(request: Request, exception: LinkHasExpired):
    return exception.response()

@app.exception_handler(InternalSQLAlchemyError)
async def exception_internal_sqlalchemy_error(request: Request, exception: InternalSQLAlchemyError):
    return exception.response()