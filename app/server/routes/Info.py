"""Info API endpoints"""

from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from .. import __version__

router = APIRouter()


@router.get(
    "/Version",
    response_description="Fetch service version",
    response_class=PlainTextResponse
)
async def get_version() -> Any:
    """Fetch service version"""
    try:
        return __version__

    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occured fetching service version"
        ) from exc
