from fastapi import APIRouter, HTTPException

from services.analytics_service import get_dashboard_data


router = APIRouter(
    prefix="/api",
    tags=["Analytics"]
)


@router.get("/analytics")
def analytics():

    data = get_dashboard_data()

    if "error" in data:

        raise HTTPException(
            status_code=500,
            detail=data
        )

    return data
