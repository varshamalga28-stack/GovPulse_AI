import requests
from config import BASE_URL


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
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


def get_prediction_history():

    try:
        response = requests.get(
            f"{BASE_URL}/api/predictions/history",
            timeout=60
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


def get_analytics():

    try:
        response = requests.get(
            f"{BASE_URL}/api/analytics",
            timeout=60
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


def get_feedback():

    try:
        response = requests.get(
            f"{BASE_URL}/api/feedback",
            timeout=60
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


def submit_feedback(data):

    try:
        response = requests.post(
            f"{BASE_URL}/api/feedback",
            json=data,
            timeout=60
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }
