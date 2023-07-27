"""Info API endpoints"""

from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from .. import __version__
from ..core import utils


router = APIRouter()
logger = utils.get_logger()


@router.get(
    "/Version",
    response_description="Fetch service version",
    response_class=PlainTextResponse,
)
async def get_version() -> Any:
    """Fetch service version"""
    try:
        logger.info("Fetching service version")
        return __version__

    except Exception as exc:
        logger.error("Error occured fetching service version")
        raise HTTPException(
            status_code=400, detail="Error occured fetching service version"
        ) from exc
