from fastapi import FastAPI

from routers.prediction import router as prediction_router
from routers.analytics import router as analytics_router
from routers.feedback import router as feedback_router


app = FastAPI(
    title="GovPulse AI Backend",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "status": "online",
        "message": "GovPulse AI Backend Running Successfully"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


app.include_router(prediction_router)
app.include_router(analytics_router)
app.include_router(feedback_router)
