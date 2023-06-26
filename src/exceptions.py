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
    
@app.exception_handler(AuthenticationFailed)
async def exception_authentication_failed(request: Request, exception: AuthenticationFailed):
    return exception.response()

@app.exception_handler(LinkAlreadyExists)
async def exception_authentication_failed(request: Request, exception: LinkAlreadyExists):
    return exception.response()

@app.exception_handler(LinkDoesNotExist)
async def exception_authentication_failed(request: Request, exception: LinkDoesNotExist):
    return exception.response()