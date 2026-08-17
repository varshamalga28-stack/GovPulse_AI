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

        if response.status_code == 200:
            return response.json()

        return {
            "error": f"Server Error ({response.status_code})",
            "details": response.text
        }

    except requests.exceptions.RequestException as e:
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

        if response.status_code == 200:
            return response.json()

        return {
            "error": f"Server Error ({response.status_code})",
            "details": response.text
        }

    except requests.exceptions.RequestException as e:
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

        if response.status_code == 200:
            return response.json()

        return {
            "error": f"Server Error ({response.status_code})",
            "details": response.text
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


# ============================================================
# Get Feedback
# ============================================================

def get_feedback():
    try:
        response = requests.get(
            f"{BASE_URL}/api/feedback",
            timeout=30
        )

        if response.status_code == 200:
            return response.json()

        return {
            "error": f"Server Error ({response.status_code})",
            "details": response.text
        }

    except requests.exceptions.RequestException as e:
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

        if response.status_code in [200, 201]:
            return response.json()

        return {
            "error": f"Server Error ({response.status_code})",
            "details": response.text
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }
