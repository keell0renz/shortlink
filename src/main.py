from .exceptions import app
from .interface import ui as ui
from .interface import api_v1 as api_v1
from .statistics import api as stat_api

app.include_router(ui.router, prefix="", tags=["User Interface"])
app.include_router(api_v1.router, prefix="/api/v1", tags=["API"])
app.include_router(
    stat_api.router,
    prefix="/statistics",
    tags=["Statistics API"])
