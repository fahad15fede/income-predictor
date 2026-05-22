# app.py

import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Income Prediction App",
    page_icon="💼",
    layout="wide"
)

# ---------------- STYLING ----------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827);
    }

    h1, h2, h3 {
        color: white;
    }

    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #1e293b;
        margin-top: 20px;
        text-align: center;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        background: #2563eb;
        color: white;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("💼 AI Income Prediction")
st.markdown("Predict whether income exceeds **50K** using Machine Learning.")

# ---------------- FORM ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 30)

    workclass = st.selectbox(
        "Workclass",
        [
            "Private", "Self-emp-not-inc", "Self-emp-inc",
            "Federal-gov", "Local-gov", "State-gov",
            "Without-pay", "Never-worked"
        ]
    )

    fnlwgt = st.number_input("Final Weight", value=100000)

    education = st.selectbox(
        "Education",
        [
            "Bachelors", "HS-grad", "Masters",
            "Some-college", "Assoc", "Doctorate"
        ]
    )

    educational_num = st.slider("Education Number", 1, 16, 10)

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Never-married",
            "Married-civ-spouse",
            "Divorced",
            "Separated",
            "Widowed"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Tech-support", "Craft-repair", "Sales",
            "Exec-managerial", "Prof-specialty",
            "Machine-op-inspct", "Adm-clerical"
        ]
    )

with col2:
    relationship = st.selectbox(
        "Relationship",
        [
            "Not-in-family",
            "Husband",
            "Wife",
            "Own-child",
            "Unmarried"
        ]
    )

    race = st.selectbox(
        "Race",
        [
            "White",
            "Black",
            "Asian-Pac-Islander",
            "Amer-Indian-Eskimo",
            "Other"
        ]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    capital_gain = st.number_input("Capital Gain", value=0)

    capital_loss = st.number_input("Capital Loss", value=0)

    hours_per_week = st.slider("Hours per Week", 1, 100, 40)

    native_country = st.selectbox(
        "Native Country",
        [
            "United-States",
            "India",
            "Pakistan",
            "Canada",
            "England",
            "Germany",
            "Philippines"
        ]
    )

# ---------------- BUTTON ----------------
if st.button("🚀 Predict Income"):

    payload = {
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "educational_num": educational_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }

    try:
        response = requests.post(
            "https://fede8rma-income-predict.hf.space/predict",
            json=payload
        )

        result = response.json()

        prediction = result["prediction"]
        probability = result["probability"]

        if prediction in [">50K", "1"]:
            msg = "💰 Predicted Income: Above 50K"
        else:
            msg = "📉 Predicted Income: Below 50K"

        st.markdown(f"""
            <div class="prediction-box">
                <h2>{msg}</h2>
                <h3>Confidence: {probability}</h3>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error connecting to API: {e}")