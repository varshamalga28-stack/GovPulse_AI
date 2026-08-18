from database import (
    get_complaints,
    get_predictions,
    get_feedback
)


def get_dashboard_data():

    try:

        # -----------------------------------------
        # GET DATA FROM SUPABASE
        # -----------------------------------------

        complaints = get_complaints()
        predictions = get_predictions()
        feedback = get_feedback()

        # -----------------------------------------
        # SAFETY CHECK
        # -----------------------------------------

        if complaints is None:
            complaints = []

        if predictions is None:
            predictions = []

        if feedback is None:
            feedback = []

        # -----------------------------------------
        # EMERGENCY COUNTS
        # -----------------------------------------

        emergency = 0
        non_emergency = 0

        for item in predictions:

            prediction = item.get("prediction")

            if str(prediction) == "1":
                emergency += 1

            else:
                non_emergency += 1

        # -----------------------------------------
        # RETURN DASHBOARD DATA
        # -----------------------------------------

        return {
            "total_complaints": len(complaints),
            "total_predictions": len(predictions),
            "total_feedback": len(feedback),
            "emergency_cases": emergency,
            "non_emergency_cases": non_emergency
        }

    except Exception as e:

        print("ANALYTICS ERROR:", repr(e))

        return {
            "error": "Analytics service failed",
            "details": str(e)
        }
