"""
API entry point
"""

from fastapi import FastAPI

from .routes.ActivityModel import router as ActivityModelRouter
from .routes.Info import router as InfoRouter
from .routes.OffTargetSearch import router as OffTargetSearchRouter


# create app and add routes
app = FastAPI()
app.include_router(ActivityModelRouter, tags=["ActivityModel"], prefix="/ActivityModel")
app.include_router(InfoRouter, tags=["Info"], prefix="/Info")
app.include_router(OffTargetSearchRouter, tags=["OffTargetSearch"], prefix="/OffTargetSearch")
