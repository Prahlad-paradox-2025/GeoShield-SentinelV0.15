from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load your pre-trained model (make sure the file is in this folder)
model = joblib.load("model_rf_geoshield.pkl")

# Define input schema
class InputData(BaseModel):
    rainfall_3day: float
    rainfall_15day: float
    ndvi_loss: float
    slope: float
    aspect: float
    proximity_to_road: float
    proximity_to_landslide: float
    in_lhz_high_risk_zone: int

@app.get("/")
def root():
    return {"message": "GeoShield Sentinel Backend is running"}

@app.post("/predict")
def predict(data: InputData):
    # Prepare data for prediction in correct order
    input_list = [[
        data.rainfall_3day,
        data.rainfall_15day,
        data.ndvi_loss,
        data.slope,
        data.aspect,
        data.proximity_to_road,
        data.proximity_to_landslide,
        data.in_lhz_high_risk_zone
    ]]
    pred = model.predict(input_list)[0]
    pred_prob = model.predict_proba(input_list)[0][1]
    return {"prediction": int(pred), "probability": float(pred_prob)} 
