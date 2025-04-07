from fastapi import FastAPI
from app.schema import LocationInput, PredictionOutput
from app.model import predict_location
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AtLocation ML API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: LocationInput):
    features = [
        input_data.latitude,
        input_data.longitude,
        input_data.speed
    ]
    label, confidence = predict_location(features)
    return {
        "predicted_location": label,
        "confidence": confidence
    }