from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd


app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Input schema matching the dataset columns (excluding 'income' target)
class PredictionInput(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    educational_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str


@app.get("/")
def root():
    return {"message": "Income Prediction API is running"}


@app.post("/predict")
def predict(data: PredictionInput):
    try:
        # Build dataframe with original column names
        input_df = pd.DataFrame([{
            "age": data.age,
            "workclass": data.workclass,
            "fnlwgt": data.fnlwgt,
            "education": data.education,
            "educational-num": data.educational_num,
            "marital-status": data.marital_status,
            "occupation": data.occupation,
            "relationship": data.relationship,
            "race": data.race,
            "gender": data.gender,
            "capital-gain": data.capital_gain,
            "capital-loss": data.capital_loss,
            "hours-per-week": data.hours_per_week,
            "native-country": data.native_country,
        }])

        prediction = model.predict(input_df)
        probability = None

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_df)
            probability = round(float(np.max(proba)), 4)

        return {
            "prediction": str(prediction[0]),
            "probability": probability
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
