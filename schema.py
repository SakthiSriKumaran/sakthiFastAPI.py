from pydantic import BaseModel

class LocationInput(BaseModel):
    user_id: str
    timestamp: str
    latitude: float
    longitude: float
    speed: float

class PredictionOutput(BaseModel):
    predicted_location: str
    confidence: float