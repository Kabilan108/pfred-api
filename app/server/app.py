"""
API entry point
"""

from fastapi import FastAPI

from .routes import ActivityModel, Info, OffTargetSearch, ScriptUtilities
from . import __version__


# create app
app = FastAPI(
    title="PFRED API", description="RNAi Enumeration and Design", version=__version__
)

# include routers
app.include_router(
    ActivityModel.router, tags=["ActivityModel"], prefix="/ActivityModel"
)
app.include_router(Info.router, tags=["Info"], prefix="/Info")
app.include_router(
    OffTargetSearch.router, tags=["OffTargetSearch"], prefix="/OffTargetSearch"
)
app.include_router(
    ScriptUtilities.router, tags=["ScriptUtilities"], prefix="/ScriptUtilities"
)
