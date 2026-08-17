from fastapi import APIRouter
from database import get_prediction_history

router = APIRouter(
    prefix="/api/predictions",
    tags=["Predictions"]
)

@router.get("/history")
def prediction_history():

    data = get_prediction_history()

    return {
        "total_predictions": len(data),
        "history": data
    }