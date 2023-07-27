"""Pydantic Models for ScriptUtilities API endpoints"""

from pydantic import BaseModel


class Orthologs(BaseModel):
    """Orthologs model"""

    ensembl_id: str
    run_directory: str
    requested_species: str
    species: str


class EnumerateFirstRequest(BaseModel):
    """Enumerate First Response"""

    secondary_transcript_ids: str
    run_directory: str
    primary_transcript_id: str
    oligo_len: int


class EnumerateSecondRequest(BaseModel):
    """Enumerate Second Response"""

    run_directory: str


class AppendToFileResponse(BaseModel):
    """Append to File Response"""

    filename: str
    text: str
    run_directory: str
