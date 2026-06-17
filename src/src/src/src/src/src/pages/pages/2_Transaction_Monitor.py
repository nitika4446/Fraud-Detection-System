import streamlit as st
import pandas as pd

st.title("💳 Transaction Monitor")

df = pd.read_csv("data/fraud_data.csv")

amount = st.slider(
    "Minimum Amount",
    0,
    10000,
    100
)

filtered = df[df["Amount"]>=amount]

st.dataframe(filtered)