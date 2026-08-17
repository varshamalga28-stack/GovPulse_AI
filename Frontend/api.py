import requests
from config import BASE_URL


# ============================================================
# Analytics
# ============================================================

def get_analytics():

    try:

        response = requests.get(
            f"{BASE_URL}/api/analytics",
            timeout=30
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Prediction History
# ============================================================

def get_prediction_history():

    try:

        response = requests.get(
            f"{BASE_URL}/api/predictions/history",
            timeout=30
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Emergency Prediction
# ============================================================

def predict_complaint(
    complaint,
    customer_name,
    email,
    phone
):

    data = {
        "complaint": complaint,
        "customer_name": customer_name,
        "email": email,
        "phone": phone
    }

    try:

        response = requests.post(
            f"{BASE_URL}/api/predict",
            json=data,
            timeout=60
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Submit Feedback
# ============================================================

def submit_feedback(
    prediction_id,
    rating,
    feedback
):

    data = {
        "prediction_id": prediction_id,
        "rating": rating,
        "feedback": feedback
    }

    try:

        response = requests.post(
            f"{BASE_URL}/api/feedback",
            json=data,
            timeout=30
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }
