import joblib
import os

MODEL_PATH = os.getenv("MODEL_PATH", "models/location_model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

def predict_location(features: list):
    pred = model.predict([features])[0]
    probas = model.predict_proba([features])[0]
    confidence = max(probas)
    return str(pred), float(confidence)