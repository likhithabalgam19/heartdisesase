import joblib
import pandas as pd

MODEL_PATH = "models/heart_disease_model.pkl"

model = joblib.load(MODEL_PATH)


def predict(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][prediction]

    return prediction, probability