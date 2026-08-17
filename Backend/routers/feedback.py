from fastapi import APIRouter
from schemas import FeedbackRequest
from database import save_feedback, get_feedback


router = APIRouter(
    prefix="/api/feedback",
    tags=["Feedback"]
)


# ============================================================
# Get all feedback
# ============================================================

@router.get("")
def feedback_list():

    data = get_feedback()

    return {
        "total_feedback": len(data),
        "feedback": data
    }


# ============================================================
# Submit feedback
# ============================================================

@router.post("")
def submit_feedback(request: FeedbackRequest):

    data = {
        "prediction_id": request.prediction_id,
        "rating": request.rating,
        "feedback": request.feedback
    }

    result = save_feedback(data)

    return {
        "message": "Feedback submitted successfully",
        "data": result
    }
