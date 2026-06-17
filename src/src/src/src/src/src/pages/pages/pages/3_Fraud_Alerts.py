import streamlit as st
import pandas as pd

st.title("🚨 Fraud Alerts")

df = pd.read_csv("data/fraud_data.csv")

alerts = df[df["Fraud"]==1]

st.error(f"{len(alerts)} Fraud Transactions Detected")

st.dataframe(alerts)