from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

# -----------------------------------
# Supabase Connection
# -----------------------------------

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------------
# Complaints
# -----------------------------------

def save_complaint(data):
    print("Sending to Supabase:", data)
    response = supabase.table("complaints").insert(data).execute()
    return response.data


def get_complaints():
    response = supabase.table("complaints").select("*").execute()
    return response.data


# -----------------------------------
# Predictions
# -----------------------------------

def save_prediction(data):
    response = supabase.table("predictions").insert(data).execute()
    return response.data


def get_predictions():
    response = supabase.table("predictions").select("*").execute()
    return response.data


def get_prediction_history():
    response = (
        supabase
        .table("predictions")
        .select("*")
        .order("predicted_at", desc=True)
        .execute()
    )
    return response.data


# -----------------------------------
# Feedback
# -----------------------------------

def save_feedback(data):
    response = supabase.table("feedback").insert(data).execute()
    return response.data


def get_feedback():
    response = supabase.table("feedback").select("*").execute()
    return response.data