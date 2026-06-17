import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

df = pd.read_csv("data/fraud_data.csv")

total_txn = len(df)

fraud_txn = len(df[df["Fraud"]==1])

fraud_rate = round(
    fraud_txn/total_txn*100,2
)

col1,col2,col3 = st.columns(3)

col1.metric("Transactions",total_txn)
col2.metric("Fraud Cases",fraud_txn)
col3.metric("Fraud Rate %",fraud_rate)

st.dataframe(df.head())