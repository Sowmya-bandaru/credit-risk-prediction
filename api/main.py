from fastapi import FastAPI
import joblib, pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from explain import explain_prediction

app = FastAPI()
model = joblib.load(os.path.join(os.path.dirname(__file__), "..", "models", "credit_risk_model.pkl"))
feature_cols = joblib.load(os.path.join(os.path.dirname(__file__), "..", "models", "feature_columns.pkl"))

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])[feature_cols]
    prob = float(model.predict_proba(df)[0][1])
    risk = "High" if prob > 0.5 else "Medium" if prob > 0.2 else "Low"
    factors = explain_prediction(model, df, feature_cols)
    return {"default_probability": round(prob, 2), "risk_category": risk, "top_factors": factors}
