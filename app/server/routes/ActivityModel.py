"""ActivityModel API endpoints"""

from typing import Any
import os

from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Query

from ..core import utils


router = APIRouter()
logger = utils.get_logger()


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


@router.post("/ASO")
async def run_aso(
    primary_id: str = Query(..., alias="PrimaryID"),
    run_directory: str = Query(..., alias="RunDirectory"),
    oligo_length: int = Query(..., alias="OligoLength"),
):
    """Run ASO activity model"""
    try:
        # TODO: Run the ASO activity model here
        # Use primary_id, run_directory, and oligo_length in the model

        return {"message": "Run ASO activity model successfully"}

    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running ASO activity model"
        ) from exc
