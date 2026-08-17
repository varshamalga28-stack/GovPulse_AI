from pydantic import BaseModel, EmailStr
from typing import Optional


class ComplaintRequest(BaseModel):
    complaint: str
    customer_name: str
    email: EmailStr
    phone: str


class PredictionResponse(BaseModel):
    prediction: int
    confidence: Optional[float] = None


class FeedbackRequest(BaseModel):
    prediction_id: int
    rating: int
    feedback: str