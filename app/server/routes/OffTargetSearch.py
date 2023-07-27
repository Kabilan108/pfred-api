"""OffTargetSearch API endpoints"""

from typing import Any
import os

from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Query

from .. import utils


router = APIRouter()
logger = utils.get_logger()


# TODO: Run siRNA Off Target Search as a background task
@router.get(
    "/siRNA",
    response_description="Run siRNA Off Target Search",
    response_class=PlainTextResponse,
)
async def run_sirna_search(
    species: str = Query(..., alias="Species", description="Species"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
    ids: str = Query(..., alias="IDs", description="IDs"),
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
            result = utils.read_file(
                os.path.join(run_directory, "sirna_search_result.csv")
            )
            return result
        except Exception as exc:  # pylint: disable=broad-except
            return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    return PlainTextResponse("siRNAOffTargetSearch.sh run failed", status_code=400)


# TODO: Run ASO as a background task
@router.get(
    "/ASO",
    response_description="Run ASO Off target search",
    response_class=PlainTextResponse,
)
async def run_aso_search(
    species: str = Query(..., alias="Species", description="Species"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
    ids: str = Query(..., alias="IDs", description="IDs"),
    miss_matches: int = Query(
        ..., alias="missMatches", description="number of allowed mismatches"
    ),
) -> Any:
    """Run siRNA Off Target Search"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    #! run_directory must point to 'scripts/'
    # create command
    cmd = f"ASOOffTargetSearch.sh {species} {ids} {miss_matches}"

    success = False

    logger.info("Running ASO search for %s", species)

    if species == "paco":
        logger.info("Shell command avoided, skipping...")
        success = True
    else:
        success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("siRNAOffTargetSearch.sh ran successfully")
        try:
            result = utils.read_file(
                os.path.join(run_directory, "aso_search_result.csv")
            )
            return result
        except Exception as exc:  # pylint: disable=broad-except
            return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    return PlainTextResponse("ASOOffTargetSearch.sh run failed", status_code=400)


@router.get(
    "/Check",
    response_description="Run Check file existence",
    response_class=PlainTextResponse,
)
async def check_file(
    file: str = Query(..., alias="File", description="File"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
) -> Any:
    """Check if file exists in run directory"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    try:
        result = utils.read_file(os.path.join(run_directory, file))
        return result
    except Exception as exc:  # pylint: disable=broad-except
        return PlainTextResponse(f"Error reading file: {exc}", status_code=400)
