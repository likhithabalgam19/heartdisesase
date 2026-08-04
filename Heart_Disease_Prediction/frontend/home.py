import streamlit as st

from frontend.styles import load_css

from backend.preprocessing import preprocess_input
from backend.predictor import predict


def home_page():

    load_css()

    st.title("❤️ Heart Disease Prediction")

    st.write("Fill all patient details below.")

    c1, c2 = st.columns(2)

    with c1:

        age = st.number_input("Age", 18, 100)

        sex = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        cp = st.selectbox(
            "Chest Pain Type",
            [
                "Typical Angina",
                "Atypical Angina",
                "Non-anginal Pain",
                "Asymptomatic"
            ]
        )

        trestbps = st.number_input(
            "Resting Blood Pressure"
        )

        chol = st.number_input(
            "Cholesterol"
        )

        fbs = st.selectbox(
            "Fasting Blood Sugar >120",
            ["No", "Yes"]
        )

    with c2:

        restecg = st.selectbox(
            "Rest ECG",
            ["Normal", "ST", "LVH"]
        )

        thalach = st.number_input(
            "Maximum Heart Rate"
        )

        exang = st.selectbox(
            "Exercise Induced Angina",
            ["No", "Yes"]
        )

        oldpeak = st.number_input(
            "Old Peak",
            step=0.1
        )

        slope = st.selectbox(
            "Slope",
            ["Upsloping", "Flat", "Downsloping"]
        )

        ca = st.slider(
            "Major Vessels",
            0,
            4
        )

        thal = st.selectbox(
            "Thal",
            [0,1,2,3]
        )

    if st.button("Predict Heart Disease"):

        sample = {

            "age": age,
            "sex": 1 if sex=="Male" else 0,
            "cp": [
                "Typical Angina",
                "Atypical Angina",
                "Non-anginal Pain",
                "Asymptomatic"
            ].index(cp),
            "trestbps": trestbps,
            "chol": chol,
            "fbs": 1 if fbs=="Yes" else 0,
            "restecg": ["Normal","ST","LVH"].index(restecg),
            "thalach": thalach,
            "exang": 1 if exang=="Yes" else 0,
            "oldpeak": oldpeak,
            "slope": ["Upsloping","Flat","Downsloping"].index(slope),
            "ca": ca,
            "thal": thal

        }

        data = preprocess_input(sample)

        prediction, probability = predict(data)

        if prediction == 1:

            st.error("⚠️ Heart Disease Detected")

        else:

            st.success("✅ No Heart Disease")

        st.metric(
            "Confidence",
            f"{probability*100:.2f}%"
        )