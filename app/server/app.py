"""
API entry point
"""

from fastapi import FastAPI

from .routes.ActivityModel import router as ActivityModelRouter


# create app and add routes
app = FastAPI()
app.include_router(ActivityModelRouter, tags=["ActivityModel"], prefix="/ActivityModel")
