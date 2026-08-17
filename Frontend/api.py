import requests
from config import BASE_URL


# ============================================================
# Common GET request
# ============================================================

def safe_get(endpoint):
    try:
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            timeout=60
        )

        print("GET:", endpoint)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text[:500])

        if response.status_code != 200:
            return {
                "error": f"Backend returned HTTP {response.status_code}",
                "details": response.text
            }

        if not response.text.strip():
            return {
                "error": "Backend returned an empty response"
            }

        try:
            return response.json()

        except ValueError:
            return {
                "error": "Backend returned invalid JSON",
                "details": response.text[:500]
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Cannot connect to backend: {str(e)}"
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# ============================================================
# Common POST request
# ============================================================

def safe_post(endpoint, data):
    try:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=data,
            timeout=60
        )

        print("POST:", endpoint)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text[:500])

        if response.status_code not in [200, 201]:
            return {
                "error": f"Backend returned HTTP {response.status_code}",
                "details": response.text
            }

        if not response.text.strip():
            return {
                "error": "Backend returned an empty response"
            }

        try:
            return response.json()

        except ValueError:
            return {
                "error": "Backend returned invalid JSON",
                "details": response.text[:500]
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": f"Cannot connect to backend: {str(e)}"
        }

    except Exception as e:
        return {
            "error": str(e)
        }


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

    return safe_post(
        "/api/predict",
        data
    )


# ============================================================
# Prediction History
# ============================================================

def get_prediction_history():

    return safe_get(
        "/api/predictions/history"
    )


# ============================================================
# Analytics
# ============================================================

def get_analytics():

    return safe_get(
        "/api/analytics"
    )


# ============================================================
# Feedback
# ============================================================

def get_feedback():

    return safe_get(
        "/api/feedback"
    )


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

    return safe_post(
        "/api/feedback",
        data
    )
