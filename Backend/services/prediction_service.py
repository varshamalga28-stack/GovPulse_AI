from predictor import predictor
from database import save_complaint, save_prediction


def predict_complaint(request):

    # Run ML prediction
    result = predictor.predict_emergency(request.complaint)

    # Save complaint
    complaint = {
        "complaint": request.complaint,
        "customer_name": request.customer_name,
        "email": request.email,
        "phone": request.phone
    }

    saved_complaint = save_complaint(complaint)

    # Get complaint ID
    complaint_id = None

    if saved_complaint:
        complaint_id = saved_complaint[0].get("id")

    # Save prediction
    prediction = {
        "complaint_id": complaint_id,
        "prediction": result.get("prediction"),
        "confidence": result.get("confidence")
    }

    save_prediction(prediction)

    return result