from fastapi import APIRouter

from database import (
    get_feedback,
    save_feedback
)


router = APIRouter(
    prefix="/api",
    tags=["Feedback"]
)


@router.get("/feedback")
def get_all_feedback():

    feedback = get_feedback()

    return {
        "total_feedback": len(feedback),
        "feedback": feedback
    }


@router.post("/feedback")
def create_feedback(data: dict):

    result = save_feedback(data)

    return {
        "message": "Feedback submitted successfully",
        "data": result
    }
