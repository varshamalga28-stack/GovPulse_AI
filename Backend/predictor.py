import os
import joblib

from config import MODEL_DIR


class Predictor:

    def __init__(self):

        print("Loading models...")

        self.emergency_model = joblib.load(
            os.path.join(MODEL_DIR, "EmergencyDetectionModel.pkl")
        )

        self.vectorizer = joblib.load(
            os.path.join(MODEL_DIR, "Emergency_Vectorizer.pkl")
        )

        print("All models loaded successfully.")

    def predict_emergency(self, text):

        prediction = self.emergency_model.predict([text])[0]

        try:
            confidence = self.emergency_model.predict_proba([text])[0].max()
            confidence = float(confidence)
        except Exception:
            confidence = None

        return {
            "prediction": int(prediction),
            "confidence": confidence
        }


predictor = Predictor()