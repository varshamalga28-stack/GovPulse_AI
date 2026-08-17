from fastapi import APIRouter
from schemas import FeedbackRequest
from database import save_feedback, get_feedback

router = APIRouter(
    prefix="/api",
    tags=["Feedback"]
)


@router.post("/feedback")
def submit_feedback(request: FeedbackRequest):
    data = {
        "prediction_id": request.prediction_id,
        "rating": request.rating,
        "feedback": request.feedback
    }

    save_feedback(data)

    return {
        "message": "Feedback submitted successfully"
    }


@router.get("/feedback")
def get_feedback_history():
    data = get_feedback()

    return {
        "total_feedback": len(data),
        "feedback": data
    }