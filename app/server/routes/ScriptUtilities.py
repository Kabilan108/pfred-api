"""ScriptUtilities API endpoints"""

from typing import Any
import os

from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, Query

from .. import utils


router = APIRouter()
logger = utils.get_logger()


# TODO: Run getOrthologs as a background task
@router.get(
    "/Orthologs",
    response_description="Run get Orthologs",
    response_class=PlainTextResponse,
)
async def get_orthologs(
    ensembl_id: str = Query(
        ..., alias="EnsemblID", description="Ensembl ID of the gene"
    ),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
    requested_species: str = Query(
        ..., alias="RequestedSpecies", description="Requested species"
    ),
    species: str = Query(..., alias="Species", description="Species"),
) -> Any:
    """Run getOrthologs.sh script"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    #! run_directory must point to 'scripts/'
    # construct command
    cmd = f"getOrthologs.sh {ensembl_id} {species} {requested_species}"
    success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("getOrthologs.sh ran successfully")
        output = os.path.join(run_directory, "seq_annotation.csv")

        try:
            result = utils.read_file(output)
            return result
        except Exception as exc:  # pylint: disable=broad-except
            return PlainTextResponse(f"Error reading file: {exc}", status_code=400)
    else:
        logger.error("getOrthologs.sh run failed")
        return PlainTextResponse("getOrthologs.sh run failed", status_code=400)


# TODO: Run Enumeration as a background task
@router.get(
    "/enumerate_first",
    response_description="Run enumerate",
    response_class=PlainTextResponse,
)
async def run_enumerate_first(
    secondary_transcript_ids: str = Query(
        ..., alias="SecondaryTranscriptIDs", description="Secondary transcript IDs"
    ),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
    primary_transcript_id: str = Query(
        ..., alias="PrimaryTranscriptID", description="Primary transcript ID"
    ),
    oligo_len: int = Query(..., alias="OligoLen", description="Oligonucleotide length"),
) -> Any:
    """Run Enumeration.sh script"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    #! run_directory must point to 'scripts/'
    # construct command
    cmd = (
        f"Enumeration.sh {secondary_transcript_ids} {primary_transcript_id} {oligo_len}"
    )
    success = utils.run_shell(cmd, run_directory)

    if success:
        logger.info("Enumeration.sh ran successfully")
        output = os.path.join(run_directory, "enumeration_result.csv")

        try:
            result = utils.read_file(output)
            return result
        except Exception as exc:  # pylint: disable=broad-except
            return PlainTextResponse(f"Error reading file: {exc}", status_code=400)
    else:
        logger.error("Enumeration.sh run failed")
        return PlainTextResponse("Enumeration.sh run failed", status_code=400)


@router.get(
    "/enumerate_second",
    response_description="Run enumerate",
    response_class=PlainTextResponse,
)
async def run_enumerate_second(
    run_name: str = Query(..., alias="RunDirectory", description="Run directory")
) -> Any:
    """Collect data from sequence.fa after running Enumeration.sh"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    # define path to sequence file
    seqfile = os.path.join(run_directory, "sequence.fa")

    try:
        if os.path.getsize(seqfile) == 0:
            return PlainTextResponse(
                "Sequence file is empty. Run /enumerate_first first.", status_code=400
            )
        else:
            result = utils.read_file(seqfile)
            return result
    except Exception as exc:  # pylint: disable=broad-except
        return PlainTextResponse(f"Error reading file: {exc}", status_code=400)


@router.get(
    "/clean",
    response_description="Run clean run directory",
    response_class=PlainTextResponse,
)
async def run_clean_run_directory(
    run_name: str = Query(..., alias="RunDirectory", description="Run directory")
) -> Any:
    """Delete a run directory"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    try:
        success = utils.remove_dir(run_directory)
        if success:
            return "Run directory removed successfully"
    except Exception as exc:  # pylint: disable=broad-except
        return PlainTextResponse(
            f"Error removing run directory: {exc}", status_code=400
        )

    return PlainTextResponse("Error removing run directory", status_code=400)


@router.get(
    "/appendToFile",
    response_description="Run append to file",
    response_class=PlainTextResponse,
)
async def run_append_to_file(
    filename: str = Query(..., alias="FileName", description="File name"),
    text: str = Query(..., alias="Text", description="Text to append"),
    run_name: str = Query(..., alias="RunDirectory", description="Run directory"),
) -> Any:
    """Append to file"""

    # create run directory
    run_directory = utils.create_run_dir(run_name)

    # define path to file
    filepath = os.path.join(run_directory, filename)

    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(text)
        return "OK"
    except Exception as exc:  # pylint: disable=broad-except
        return PlainTextResponse(f"Error appending to file: {exc}", status_code=400)
