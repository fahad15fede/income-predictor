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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0a0f1e 0%, #0d1b2a 40%, #1a0a2e 100%);
        min-height: 100vh;
    }

    /* Title */
    h1 {
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }

    h2, h3 { color: #e2e8f0 !important; }

    p, label, .stMarkdown { color: #94a3b8 !important; }

    /* Cards around columns */
    div[data-testid="column"] {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 24px !important;
        backdrop-filter: blur(10px);
    }

    /* Inputs */
    .stSelectbox > div > div,
    .stNumberInput > div > div > input,
    .stSlider {
        background: rgba(255,255,255,0.06) !important;
        border-radius: 10px !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }

    /* Slider accent */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background: linear-gradient(135deg, #a78bfa, #60a5fa) !important;
        border: none !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 14px;
        height: 56px;
        background: linear-gradient(135deg, #7c3aed, #2563eb, #0891b2);
        color: white;
        font-size: 17px;
        font-weight: 600;
        border: none;
        letter-spacing: 0.3px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 24px rgba(124, 58, 237, 0.4);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.6);
        background: linear-gradient(135deg, #6d28d9, #1d4ed8, #0e7490);
    }

    /* Prediction result box */
    .prediction-box {
        padding: 32px;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(37,99,235,0.2));
        border: 1px solid rgba(167,139,250,0.3);
        margin-top: 24px;
        text-align: center;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.2);
    }

    .prediction-box h2 {
        font-size: 1.8rem !important;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px !important;
    }

    .prediction-box p {
        color: #94a3b8 !important;
        font-size: 0.9rem;
    }

    /* Divider */
    hr { border-color: rgba(255,255,255,0.08) !important; }
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
            "Bachelors", "Some-college", "11th", "HS-grad",
            "Prof-school", "Assoc-acdm", "Assoc-voc", "9th",
            "7th-8th", "12th", "Masters", "1st-4th", "10th",
            "Doctorate", "5th-6th", "Preschool"
        ]
    )

    educational_num = st.slider("Education Number", 1, 16, 10)

    marital_status = st.selectbox(
        "Marital Status",
        [
            "Never-married", "Married-civ-spouse", "Divorced",
            "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Tech-support", "Craft-repair", "Other-service", "Sales",
            "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
            "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
            "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"
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
        confidence_note = result.get("confidence_note", "")

        if prediction == ">50K":
            msg = "💰 Predicted Income: Above 50K"
        else:
            msg = "📉 Predicted Income: Below 50K"

        st.markdown(f"""
            <div class="prediction-box">
                <h2>{msg}</h2>
                <p>{confidence_note}</p>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error connecting to API: {e}")