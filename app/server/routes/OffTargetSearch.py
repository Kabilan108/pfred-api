"""OffTargetSearch API endpoints"""

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()


@router.get("/ASO", response_description="Run ASO Off Target Search")
async def run_aso_search(
    species: str = Query(..., alias="Species"),
    run_directory: str = Query(..., alias="RunDirectory"),
    ids: str = Query(..., alias="IDs"),
    missmatch: int = Query(..., alias="missMatches"),
):
    """Run ASO Off Target Search"""
    try:
        # TODO: Run the ASO Off Target Search here
        # Use species, run_directory, ids, and missmatches in the model

        return {"message": "Run ASO Off Target Search successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running ASO Off Target Search"
        ) from exc


@router.get("/Check", response_description="Run Check file existence")
async def check_file(
    file: str = Query(..., alias="File"),
    run_directory: str = Query(..., alias="RunDirectory"),
):
    """Run Check file existence"""
    try:
        # TODO: Run the Check file existence here
        # Use file and run_directory in the model

        return {"message": "Run Check file existence successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running Check file existence"
        ) from exc


@router.get("/siRNA", response_description="Run siRNA Off Target Search")
async def run_sirna_search(
    species: str = Query(..., alias="Species"),
    run_directory: str = Query(..., alias="RunDirectory"),
    ids: str = Query(..., alias="IDs"),
    missmatch: int = Query(..., alias="missMatches"),
):
    """Run siRNA Off Target Search"""
    try:
        # TODO: Run the siRNA Off Target Search here
        # Use species, run_directory, ids, and missmatches in the model

        return {"message": "Run siRNA Off Target Search successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running siRNA Off Target Search"
        ) from exc
