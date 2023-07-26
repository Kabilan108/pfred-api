"""Schema for /Info endpoint"""

from pydantic import BaseModel


class VersionResponse(BaseModel):
    """Version response schema"""
    version: str
