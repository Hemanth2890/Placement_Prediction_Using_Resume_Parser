import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb
import joblib
import os
import sidebar

st.set_page_config(page_title="Placement Prediction", layout="wide")

sidebar.load_sidebar()

page_bg = """
<style>
body {
    background-image: url('https://i.pinimg.com/originals/1a/a2/00/1aa2008c04d15f46d38b797cb1452ed4.gif');
    background-size: cover;
    background-attachment: fixed;
    color: #fff;
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 20px;
    border-radius: 10px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🎓 Placement & Package Prediction Bot")
st.write("Enter your details to predict placement chances and expected salary package.")

if os.path.exists("placement_prediction_model.pkl") and os.path.exists("xgb_package_model.json") and os.path.exists("scaler.pkl") and os.path.exists("scaler_package.pkl"):
    placement_model = joblib.load("placement_prediction_model.pkl")
    package_model = xgb.XGBRegressor()
    package_model.load_model("xgb_package_model.json")
    scaler = joblib.load("scaler.pkl")
    scaler_package = joblib.load("scaler_package.pkl")
else:
    st.error("❌ Model files not found! Please check the file paths.")
    st.stop()

feature_columns = [
    "CGPA", "Backlogs", "10th Percentage", "12th Percentage", 
    "Internships", "Coding Score", "Certifications", 
    "Communication Skill", "Hackathon Participation", "Applications Submitted"
]

if "user_inputs" not in st.session_state:
    st.session_state.user_inputs = {
        "CGPA": 7.0,
        "Backlogs": 0,
        "10th Percentage": 85.0,
        "12th Percentage": 80.0,
        "Internships": 1,
        "Coding Score": 500,
        "Certifications": 1,
        "Communication Skill": 3,
        "Hackathon Participation": 0,
        "Applications Submitted": 10,
    }

st.session_state.user_inputs["CGPA"] = st.number_input("CGPA (0-10)", min_value=0.0, max_value=10.0, step=0.1, value=st.session_state.user_inputs["CGPA"])
st.session_state.user_inputs["Backlogs"] = st.number_input("Number of Backlogs", min_value=0, max_value=49, step=1, value=st.session_state.user_inputs["Backlogs"])
st.session_state.user_inputs["10th Percentage"] = st.number_input("10th Percentage (60-100)", min_value=60.0, max_value=100.0, step=0.1, value=st.session_state.user_inputs["10th Percentage"])
st.session_state.user_inputs["12th Percentage"] = st.number_input("12th Percentage (60-100)", min_value=60.0, max_value=100.0, step=0.1, value=st.session_state.user_inputs["12th Percentage"])
st.session_state.user_inputs["Internships"] = st.slider("Number of Internships", min_value=0, max_value=5, step=1, value=st.session_state.user_inputs["Internships"])
st.session_state.user_inputs["Coding Score"] = st.number_input("Coding Score (200-800)", min_value=200, max_value=800, step=10, value=st.session_state.user_inputs["Coding Score"])
st.session_state.user_inputs["Certifications"] = st.selectbox("Certifications", [0, 1, 2], index=st.session_state.user_inputs["Certifications"], format_func=lambda x: ["None", "Basic", "Advanced"][x])
st.session_state.user_inputs["Communication Skill"] = st.slider("Communication Skill (1-5)", min_value=1, max_value=5, step=1, value=st.session_state.user_inputs["Communication Skill"])
st.session_state.user_inputs["Hackathon Participation"] = st.selectbox("Hackathon Participation", [0, 1], index=st.session_state.user_inputs["Hackathon Participation"], format_func=lambda x: ["No", "Yes"][x])
st.session_state.user_inputs["Applications Submitted"] = st.number_input("Job Applications Submitted", min_value=0, max_value=100, step=1, value=st.session_state.user_inputs["Applications Submitted"])

if st.button("Predict Placement"):
    user_input_df = pd.DataFrame([st.session_state.user_inputs])

    user_input_scaled = scaler.transform(user_input_df)
    placement_prediction = placement_model.predict(user_input_scaled)[0]

    if placement_prediction == 1:
        user_input_scaled_p = scaler_package.transform(user_input_df)
        predicted_package = package_model.predict(user_input_scaled_p)[0]
        st.success(f"✅ Placed! Expected Package: ₹{predicted_package:.2f} LPA")
    else:
        st.error("❌ Not Placed. Keep improving your skills!")
