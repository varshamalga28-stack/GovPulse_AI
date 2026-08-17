import os
import joblib

from config import MODEL_DIR

print("MODEL DIRECTORY")
print(MODEL_DIR)

print("\nFILES")

for f in os.listdir(MODEL_DIR):
    print(f)

print("\nLoading Emergency Model...")

model = joblib.load(
    os.path.join(
        MODEL_DIR,
        "EmergencyDetectionModel.pkl"
    )
)

print(type(model))

print("\nSUCCESS")