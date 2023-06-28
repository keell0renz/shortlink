from .exceptions import app
from .interface import ui as ui
from .interface import api as api
from .statistics import api as stat_api

app.include_router(ui.router, prefix="", tags=["User Interface"])
app.include_router(api.router, prefix="/api", tags=["API"])
app.include_router(stat_api.router, prefix="/statistics", tags=["Statistics API"])