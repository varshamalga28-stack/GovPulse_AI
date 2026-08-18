import requests

from config import BASE_URL


# ============================================================
# BACKEND CONNECTION
# ============================================================

def check_backend():
    """
    Check whether the FastAPI backend is reachable.
    """
    try:
        response = requests.get(
            f"{BASE_URL}/",
            timeout=30
        )

        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            return {
                "message": response.text
            }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


# ============================================================
# ANALYTICS
# ============================================================

def get_analytics():

    try:

        response = requests.get(
            f"{BASE_URL}/api/analytics",
            timeout=60
        )

        response.raise_for_status()

        try:
            return response.json()

        except ValueError:

            return {
                "error": (
                    "Backend returned a non-JSON response. "
                    f"Status: {response.status_code}"
                )
            }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }


# ============================================================
# PREDICTION HISTORY
# ============================================================

def get_prediction_history():

    try:

        response = requests.get(
            f"{BASE_URL}/api/predictions/history",
            timeout=60
        )

        response.raise_for_status()

        try:
            return response.json()

        except ValueError:

            return {
                "error": (
                    "Backend returned a non-JSON response."
                )
            }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }


# ============================================================
# PREDICTION
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

        response.raise_for_status()

        try:
            return response.json()

        except ValueError:

            return {
                "error": (
                    "Backend returned a non-JSON response."
                )
            }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }


# ============================================================
# FEEDBACK
# ============================================================

def get_feedback():

    try:

        response = requests.get(
            f"{BASE_URL}/api/feedback",
            timeout=60
        )

        response.raise_for_status()

        try:
            return response.json()

        except ValueError:

            return {
                "error": (
                    "Backend returned a non-JSON response."
                )
            }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }


# ============================================================
# SUBMIT FEEDBACK
# ============================================================

def submit_feedback(
    prediction_id,
    rating,
    comments
):

    data = {
        "prediction_id": prediction_id,
        "rating": rating,
        "comments": comments
    }

    try:

        response = requests.post(
            f"{BASE_URL}/api/feedback",
            json=data,
            timeout=60
        )

        response.raise_for_status()

        try:
            return response.json()

        except ValueError:

            return {
                "error": (
                    "Backend returned a non-JSON response."
                )
            }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }
