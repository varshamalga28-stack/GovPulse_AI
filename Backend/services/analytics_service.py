from database import get_complaints, get_predictions, get_feedback


def get_dashboard_data():

    complaints = get_complaints()
    predictions = get_predictions()
    feedback = get_feedback()

    emergency = 0
    non_emergency = 0

    for item in predictions:
        if item.get("prediction") == 1:
            emergency += 1
        else:
            non_emergency += 1

    return {
        "total_complaints": len(complaints),
        "total_predictions": len(predictions),
        "total_feedback": len(feedback),
        "emergency_cases": emergency,
        "non_emergency_cases": non_emergency
    }