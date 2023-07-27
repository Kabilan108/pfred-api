"""Pydantic Models for ScriptUtilities API endpoints"""

from pydantic import BaseModel


class OrthologsParams(BaseModel):
    """Parameters for get Orthologs"""

    ensembl_id: str
    run_directory: str
    requested_species: str
    species: str


class EnumerateFirstParams(BaseModel):
    """Parameters for enumerate"""

    secondary_transcript_ids: str
    run_directory: str
    primary_transcript_id: str
    oligo_len: int


class EnumerateSecondRequest(BaseModel):
    """Parameters for enumerate"""

    run_directory: str


class CleanRunDirParams(BaseModel):
    """Parameters for clean run directory"""

    run_directory: str


class AppendToFileResponse(BaseModel):
    """Response for append to file"""

    filename: str
    text: str
    run_directory: str
