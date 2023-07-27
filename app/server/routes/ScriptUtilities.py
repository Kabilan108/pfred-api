"""ScriptUtilities API endpoints"""

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()


@router.get("/Orthologs", response_description="Run get Orthologs")
async def run_get_orthologs(
    ensembl_id: str = Query(..., alias="EnsemblID"),
    run_directory: str = Query(..., alias="RunDirectory"),
    requested_species: str = Query(..., alias="RequestedSpecies"),
    species: str = Query(..., alias="Species"),
):
    """Run get Orthologs"""
    try:
        # TODO: Run the get Orthologs here
        # Use ensembl_id, run_directory, requested_species, and species in the model

        return {"message": "Run get Orthologs successfully"}
    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running get Orthologs"
        ) from exc


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
