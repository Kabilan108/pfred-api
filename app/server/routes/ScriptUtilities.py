"""ScriptUtilities API endpoints"""

from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

import os
import aiofiles

from ..models.ScriptUtilities import (
    OrthologsParams,
    EnumerateFirstParams,
    EnumerateSecondRequest,
    CleanRunDirParams,
    AppendToFileResponse,
)
from ..core import utils


router = APIRouter()
logger = utils.get_logger()


@router.get(
    "/Orthologs",
    response_description="Run get Orthologs",
    response_class=PlainTextResponse,
)
async def get_orthologs(
    ensembl_id: str = Query(
        ..., alias="EnsemblID", description="Ensembl ID of the gene"
    ),
    run_name: str = Query(
        ..., alias="RunDirectory", description="Run directory"
    ),
    requested_species: str = Query(
        ..., alias="RequestedSpecies", description="Requested species"
    ),
    species: str = Query(
        ..., alias="Species", description="Species"
    ),
) -> Any:
    """Run getOrthologs.sh script"""
    try:
        # create run directory
        run_directory = utils.create_run_dir(run_name)

        #! run_directory must point to 'scripts/'
        # construct command
        cmd = f"getOrthologs.sh {ensembl_id} {species} {requested_species}"
        success = utils.run_shell(cmd, run_directory)

        if success:
            logger.info("getOrthologs.sh ran successfully")
            output = os.path.join(run_directory, "seq_annotations.csv")

            try:
                result = utils.read_file(output)
                return result
            except Exception as exc:  # pylint: disable=broad-except
                return PlainTextResponse(f"Error reading file: {exc}", status_code=400)

    except Exception as exc:  # pylint: disable=broad-except
        return PlainTextResponse(f"getOrthologs.sh run failed: {exc}", status_code=400)


@router.get("/enumerate_first", response_description="Run enumerate")
async def run_enumerate_first(
    secondary_transcript_ids: str = Query(..., alias="SecondaryTranscriptIDs"),
    run_directory: str = Query(..., alias="RunDirectory"),
    primary_transcript_id: str = Query(..., alias="PrimaryTranscriptID"),
    oligo_len: int = Query(..., alias="OligoLen"),
):
    """Run enumerate"""
    try:
        # TODO: Run enumerate here
        # Use secondary_transcript_ids, run_directory, primary_transcript_id, and oligo_len in the model

        return {"message": "Run enumerate successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running enumerate"
        ) from exc


@router.get("/enumerate_second", response_description="Run enumerate")
async def run_enumerate_second(run_directory: str = Query(..., alias="RunDirectory")):
    """Run enumerate"""
    try:
        # TODO: Run enumerate here
        # Use run_directory in the model

        return {"message": "Run enumerate successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running enumerate"
        ) from exc


@router.get("/clean", response_description="Run clean run directory")
async def run_clean_run_directory(
    run_directory: str = Query(..., alias="RunDirectory")
):
    """Run clean run directory"""
    try:
        # TODO: Run clean run directory here
        # Use run_directory in the model

        return {"message": "Run clean run directory successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running clean run directory"
        ) from exc


@router.get("/appendToFile", response_description="Run append to file")
async def run_append_to_file(
    filename: str = Query(..., alias="FileName"),
    text: str = Query(..., alias="Text"),
    run_directory: str = Query(..., alias="RunDirectory"),
):
    """Run append to file"""
    try:
        # TODO: Run append to file here
        # Use filename, text, and run_directory in the model

        return {"message": "Run append to file successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running append to file"
        ) from exc
