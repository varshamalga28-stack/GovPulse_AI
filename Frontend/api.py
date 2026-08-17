import requests
from config import BASE_URL


# ============================================================
# Helper function
# ============================================================

def _get_json(response):
    """
    Safely convert a response to JSON.
    Prevents JSON decode errors when Render returns
    an empty/non-JSON response.
    """

    try:
        return response.json()

    except ValueError:
        return {
            "error": f"Backend returned non-JSON response "
                     f"(HTTP {response.status_code})",
            "response_text": response.text[:500]
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

    try:

        response = requests.post(
            f"{BASE_URL}/api/predict",
            json=data,
            timeout=60
        )

        return _get_json(response)

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Backend connection error: {str(e)}"
        }

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

        return _get_json(response)

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Backend connection error: {str(e)}"
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Analytics
# ============================================================

def get_analytics():

    try:

        response = requests.get(
            f"{BASE_URL}/api/analytics",
            timeout=30
        )

        return _get_json(response)

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Backend connection error: {str(e)}"
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Feedback - GET
# ============================================================

def get_feedback():

    try:

        response = requests.get(
            f"{BASE_URL}/api/feedback",
            timeout=30
        )

        return _get_json(response)

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Backend connection error: {str(e)}"
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# ============================================================
# Feedback - POST
# ============================================================

def submit_feedback(data):

    try:

        response = requests.post(
            f"{BASE_URL}/api/feedback",
            json=data,
            timeout=30
        )

        return _get_json(response)

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Backend connection error: {str(e)}"
        }

    except Exception as e:

        return {
            "error": str(e)
        }
