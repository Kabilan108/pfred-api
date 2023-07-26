"""ActivityModel API endpoints"""

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()


@router.post("/siRNA")
async def run_sirna(
    primary_id: str = Query(..., alias="PrimaryID"),
    run_directory: str = Query(..., alias="RunDirectory"),
):
    """Run siRNA activity model"""
    try:
        # TODO: Run the siRNA activity model here
        # Use primary_id and run_directory in the model

        return {"message": "Run siRNA activity model successfully"}

    except Exception as exc:
        raise HTTPException(
            status_code=400, detail="Error occurred in running siRNA activity model"
        ) from exc


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
