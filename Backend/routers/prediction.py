from fastapi import APIRouter
from schemas import ComplaintRequest
from services.prediction_service import predict_complaint
from database import get_prediction_history

router = APIRouter(
    prefix="/api",
    tags=["Prediction"]
)


@router.post("/predict")
def predict(request: ComplaintRequest):
    return predict_complaint(request)


@router.get("/predictions/history")
def prediction_history():

    data = get_prediction_history()

    return {
        "total_predictions": len(data),
        "history": data
    }