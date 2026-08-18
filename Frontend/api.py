import requests
from config import BASE_URL


# ============================================================
# Helper function
# ============================================================

def _get_json(endpoint, timeout=60):
    try:
        url = f"{BASE_URL}{endpoint}"

        response = requests.get(
            url,
            timeout=timeout,
            headers={
                "Accept": "application/json"
            }
        )

        response.raise_for_status()

        # Check whether the response actually contains JSON
        try:
            return response.json()
        except ValueError:
            return {
                "error": f"Backend returned non-JSON response: {response.text[:500]}"
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Backend connection error: {str(e)}"
        }


def _post_json(endpoint, data, timeout=60):
    try:
        url = f"{BASE_URL}{endpoint}"

        response = requests.post(
            url,
            json=data,
            timeout=timeout,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )

        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            return {
                "error": f"Backend returned non-JSON response: {response.text[:500]}"
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Backend connection error: {str(e)}"
        }


# ============================================================
# Analytics
# ============================================================

def get_analytics():
    return _get_json("/api/analytics")


# ============================================================
# Prediction History
# ============================================================

def get_prediction_history():
    return _get_json("/api/predictions/history")


# ============================================================
# Feedback
# ============================================================

def get_feedback():
    return _get_json("/api/feedback")


def submit_feedback(data):
    return _post_json("/api/feedback", data)


# ============================================================
# Prediction
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

    return _post_json(
        "/api/predict",
        data,
        timeout=120
    )
