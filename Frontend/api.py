import requests

from config import BASE_URL


TIMEOUT = 10


def get_analytics():
    try:
        response = requests.get(
            f"{BASE_URL}/api/analytics",
            timeout=TIMEOUT
        )

        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {"error": str(e)}


def get_prediction_history():
    try:
        response = requests.get(
            f"{BASE_URL}/api/predictions/history",
            timeout=TIMEOUT
        )

        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {"error": str(e)}


def get_feedback():
    try:
        response = requests.get(
            f"{BASE_URL}/api/feedback",
            timeout=TIMEOUT
        )

        response.raise_for_status()
        return response.json()

    except Exception as e:
        return {"error": str(e)}


def predict_complaint(
    complaint,
    customer_name,
    email,
    phone
):

    payload = {
        "complaint": complaint,
        "customer_name": customer_name,
        "email": email,
        "phone": phone
    }

    try:
        response = requests.post(
            f"{BASE_URL}/api/predict",
            json=payload,
            timeout=TIMEOUT
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}


def submit_feedback(
    prediction_id,
    rating,
    feedback
):

    payload = {
        "prediction_id": prediction_id,
        "rating": rating,
        "feedback": feedback
    }

    try:
        response = requests.post(
            f"{BASE_URL}/api/feedback",
            json=payload,
            timeout=TIMEOUT
        )

        return response.json()

    except Exception as e:
        return {"error": str(e)}