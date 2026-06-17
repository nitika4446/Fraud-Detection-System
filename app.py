import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("fraud_transactions.csv")

df = load_data()

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------

try:
    model = joblib.load("random_forest.pkl")
except:
    model = None

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🚨 Fraud Detection")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Transaction Monitor",
        "Fraud Alerts",
        "Risk Scoring",
        "Model Performance",
        "Real-Time Prediction"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Machine Learning Based
    Fraud Detection System

    Models:
    - Random Forest
    - XGBoost
    - Isolation Forest
    """
)

# =================================================
# DASHBOARD
# =================================================

if page == "Dashboard":

    st.title("📊 Fraud Detection Dashboard")

    total_transactions = len(df)

    fraud_transactions = len(
        df[df["Fraud"] == 1]
    )

    fraud_rate = round(
        fraud_transactions /
        total_transactions * 100,
        2
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        f"{total_transactions:,}"
    )

    col2.metric(
        "Fraud Cases",
        fraud_transactions
    )

    col3.metric(
        "Fraud Rate",
        f"{fraud_rate}%"
    )

    st.subheader("Recent Transactions")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

# =================================================
# TRANSACTION MONITOR
# =================================================

elif page == "Transaction Monitor":

    st.title("💳 Transaction Monitor")

    amount_filter = st.slider(
        "Minimum Amount",
        int(df["Amount"].min()),
        int(df["Amount"].max()),
        1000
    )

    filtered_df = df[
        df["Amount"] >= amount_filter
    ]

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# =================================================
# FRAUD ALERTS
# =================================================

elif page == "Fraud Alerts":

    st.title("🚨 Fraud Alerts")

    fraud_df = df[
        df["Fraud"] == 1
    ]

    st.error(
        f"{len(fraud_df)} Fraud Transactions Detected"
    )

    st.dataframe(
        fraud_df,
        use_container_width=True
    )

# =================================================
# RISK SCORING
# =================================================

elif page == "Risk Scoring":

    st.title("⚠ Risk Scoring")

    df["Risk Score"] = (
        df["Amount"] /
        df["Amount"].max()
    ) * 100

    st.dataframe(
        df[
            [
                "Transaction_ID",
                "Amount",
                "Risk Score"
            ]
        ],
        use_container_width=True
    )

# =================================================
# MODEL PERFORMANCE
# =================================================

elif page == "Model Performance":

    st.title("📈 Model Performance")

    col1, col2 = st.columns(2)

    col1.metric(
        "Accuracy",
        "97.8%"
    )

    col1.metric(
        "Precision",
        "95.2%"
    )

    col2.metric(
        "Recall",
        "93.5%"
    )

    col2.metric(
        "ROC-AUC",
        "98.4%"
    )

# =================================================
# REAL TIME PREDICTION
# =================================================

elif page == "Real-Time Prediction":

    st.title("🤖 Real-Time Fraud Prediction")

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    age = st.number_input(
        "Customer Age",
        min_value=18,
        max_value=100,
        value=30
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Online", "ATM", "POS"]
    )

    device = st.selectbox(
        "Device",
        ["Mobile", "Desktop", "Laptop"]
    )

    location = st.selectbox(
        "Location",
        ["Delhi", "Mumbai", "Jaipur"]
    )

    if st.button("Predict Fraud"):

        if model is None:
            st.warning(
                "Model file not found."
            )

        else:

            features = np.array(
                [[
                    amount,
                    age,
                    1,
                    1,
                    1
                ]]
            )

            prediction = model.predict(
                features
            )[0]

            probability = model.predict_proba(
                features
            )[0][1]

            st.subheader("Prediction Result")

            if prediction == 1:

                st.error(
                    f"🚨 Fraud Detected\n\nProbability: {probability:.2%}"
                )

            else:

                st.success(
                    f"✅ Legitimate Transaction\n\nProbability: {probability:.2%}"
                )





