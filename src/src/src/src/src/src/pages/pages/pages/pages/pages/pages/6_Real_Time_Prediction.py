import streamlit as st
import numpy as np
import joblib

st.title("🤖 Real-Time Prediction")

model = joblib.load(
    "models/random_forest.pkl"
)

amount = st.number_input(
    "Transaction Amount",
    0.0,
    100000.0
)

age = st.number_input(
    "Customer Age",
    18,
    90
)

if st.button("Predict"):

    features = np.array(
        [[amount,age,1,1,1]]
    )

    prediction = model.predict(
        features
    )[0]

    prob = model.predict_proba(
        features
    )[0][1]

    if prediction == 1:
        st.error(
            f"Fraud Detected ({prob:.2%})"
        )
    else:
        st.success(
            f"Legitimate ({prob:.2%})"
        )