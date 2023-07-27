"""OffTargetSearch API endpoints"""

from typing import Any
import os

from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Query

from ..core import utils


router = APIRouter()
logger = utils.get_logger()


@router.get(
    "/siRNA",
    response_description="Run siRNA Off Target Search",
    response_class=PlainTextResponse
)
async def run_sirna_search(
    species: str = Query(
        ..., alias="Species", description="Species"
    ),
    run_name: str = Query(
        ..., alias="RunDirectory", description="Run directory"
    ),
    ids: str = Query(
        ..., alias="IDs", description="IDs"
    ),
    miss_matches: int = Query(
        ..., alias="missMatches", description="number of allowed mismatches"
    ),
) -> Any:
    """Run siRNA Off Target Search"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    #! run_directory must point to 'scripts/'
    # create command
    cmd = f"siRNAOffTargetSearch.sh {species} {ids} {miss_matches}"

    success = False

    logger.info("Running siRNA search for %s", species)

    if species == "paco":
        logger.info("Shell command avoided, skipping...")
        success = True
    else:
        success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("siRNAOffTargetSearch.sh ran successfully")
        try:
            result = utils.read_file(os.path.join(run_directory, "sirna_search_result.csv"))
            return result
        except Exception as exc:  # pylint: disable=broad-except
            return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    return PlainTextResponse("siRNAOffTargetSearch.sh run failed", status_code=400)


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



