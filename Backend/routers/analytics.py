from fastapi import APIRouter
from services.analytics_service import get_dashboard_data

router = APIRouter(
    prefix="/api",
    tags=["Analytics"]
)

@router.get("/analytics")
def analytics():
    return get_dashboard_data()