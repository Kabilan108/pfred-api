"""ActivityModel API endpoints"""

from typing import Any
import os

from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Query

from ..core import utils


router = APIRouter()
logger = utils.get_logger()


# TODO: Run siRNA activity model as a background task
@router.post(
    "/siRNA",
    responses={
        200: {"description": "Run siRNA activity model successfully"}, 
        400: {"description": "Error occurred in running siRNA activity model"}
    },
    response_class=PlainTextResponse
)
async def run_sirna_activity_model(
    primary_id: str = Query(..., alias="PrimaryID", description="Primary ID"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory")
) -> Any:
    """Run siRNA activity model"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    # get script path
    scripts_dir = utils.get_scripts_dir()

    #! run_directory must point to 'scripts/'
    #! scripts_dir must contain 'siRNA_2431seq_modelBuilding.csv'
    # construct command
    cmd  = f"getSeqGivenTrans.sh {primary_id}"

    # run command
    success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("getSeqGivenTrans.sh ran successfully")

        # copy modelBuilding.csv to run_directory
        utils.copyfile(os.path.join(scripts_dir, "siRNA_2431seq_modelBuilding.csv"), run_directory)

        success = utils.run_shell("siRNAActivityModel.sh", run_directory)

        if success:
            logger.info("siRNAActivityModel.sh ran successfully")
            try:
                result = utils.read_file(os.path.join(run_directory, "siRNAActivityModel.csv"))
                return result
            except Exception as exc:  # pylint: disable=broad-except
                logger.error("Error reading file: %s", exc)
                return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    return PlainTextResponse("getSeqGivenTrans.sh run failed", status_code=400)


# TODO: Run ASO as a background task
@router.post(
    "/ASO",
    responses={
        200: {"description": "Run ASO activity model successfully"},
        400: {"description": "Error occurred in running siRNA activity model"}
    },
    response_class=PlainTextResponse
)
async def run_aso_activity_model(
    primary_id: str = Query(..., alias="PrimaryID", description="Primary ID"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory")
) -> Any:
    """Run siRNA activity model"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    # get script path
    scripts_dir = utils.get_scripts_dir()

    #! run_directory must point to 'scripts/'
    #! scripts_dir must contain 'siRNA_2431seq_modelBuilding.csv'
    # construct command``
    cmd  = f"getSeqGivenTrans.sh {primary_id}"

    # run command
    success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("getSeqGivenTrans.sh ran successfully")

        # copy files to run_directory
        utils.copyfile(os.path.join(scripts_dir, "input_15_21_100_1000_12.txt"), run_directory)
        utils.copyfile(os.path.join(scripts_dir, "AOBase_542seq_cleaned_modelBuilding_Jan2009_15_21_noOutliers.csv"), run_directory)

        success = utils.run_shell("ASOActivityModel.sh", run_directory)

        if success:
            logger.info("ASOActivityModel.sh ran successfully")
            try:
                result = utils.read_file(os.path.join(run_directory, "ASOActivityModelResult.csv"))
                return result
            except Exception as exc:  # pylint: disable=broad-except
                logger.error("Error reading file: %s", exc)
                return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    return PlainTextResponse("getSeqGivenTrans.sh run failed", status_code=400)
