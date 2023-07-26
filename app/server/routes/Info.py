"""Info API endpoints"""

from typing import Any

from fastapi import APIRouter, HTTPException

from .. import __version__
from ..models.Info import VersionResponse

router = APIRouter()


@router.get("/Version", response_description="Fetch service version", response_model=VersionResponse)
async def get_version() -> Any:
    """Fetch service version"""
    try:
        return {"version": __version__}

    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occured fetching service version"
        ) from exc
