import streamlit as st
import sidebar

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

st.title("🚀 Welcome to the Placement Prediction Bot!")
st.write(
    """
    In today's competitive job market, it's essential to understand where you stand.
    
    **What this bot does:**
    - 📊 Predicts your placement chances based on various key factors.
    - 💰 Estimates your expected salary based on your profile.
    - 🎯 Provides insights into improving your profile for better opportunities.

    **How it works:**
    - Fill in details about your academics, internships, coding skills, and more.
    - Our AI model, trained on real placement data, predicts your chances.
    - Get an estimated package and plan your next move accordingly.

    Ready to see your placement potential? Click the button below to start! 🎯
    """
)

if st.button("🚀 Start Prediction"):
    st.switch_page("pages/prediction.py")
