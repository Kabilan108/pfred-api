"""
API entry point
"""

from fastapi import FastAPI

from .routes.ActivityModel import router as ActivityModelRouter
from .routes.Info import router as InfoRouter
from .routes.OffTargetSearch import router as OffTargetSearchRouter
from .routes.ScriptUtilities import router as ScriptUtilitiesRouter
from . import __version__


# create app
app = FastAPI(
    title="PFRED API",
    description="RNAi Enumeration and Design",
    version=__version__
)

# include routers
app.include_router(ActivityModelRouter, tags=["ActivityModel"], prefix="/ActivityModel")
app.include_router(InfoRouter, tags=["Info"], prefix="/Info")
app.include_router(OffTargetSearchRouter, tags=["OffTargetSearch"], prefix="/OffTargetSearch")
app.include_router(ScriptUtilitiesRouter, tags=["ScriptUtilities"], prefix="/ScriptUtilities")
