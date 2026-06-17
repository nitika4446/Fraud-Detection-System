import streamlit as st
import pandas as pd

st.title("⚠ Risk Scoring")

df = pd.read_csv("data/fraud_data.csv")

df["Risk Score"] = (
    df["Amount"] /
    df["Amount"].max()
)*100

st.dataframe(
    df[
        ["Transaction_ID",
        "Amount",
        "Risk Score"]
    ]
)