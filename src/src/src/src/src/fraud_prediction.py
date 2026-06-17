import joblib
import numpy as np

model = joblib.load("models/random_forest.pkl")

def predict_fraud(data):

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    return prediction, probability