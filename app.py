import streamlit as st
import sidebar

st.set_page_config(page_title="Placement Prediction Bot", layout="wide")

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

sidebar.load_sidebar()

st.title("🚀 Welcome to the Placement Prediction Bot!")

st.write(
    """
    In today's competitive job market, understanding your strengths and weaknesses can be the key to landing your dream job. That's where we come in!
    
    ### 🤖 What our bot does:
    - ✅ **Predicts your placement chances** – Wondering if you're placement-ready? We analyze multiple key factors to give you a clear idea of where you stand.
    - 💰 **Estimates your expected salary** – Get an approximate salary package based on your skills, academics, and experience.
    - 📄 **ATS Analysis** – Analyzes your resume and gives you valuable insights based on the job description, and also gives suggestions on how to improve your resume.
    
    ### 🚀 How does it work?
    - 🔹 **Fill in details** about your academics, internships, coding skills, certifications, and more.
    - 🔹 Our **AI model**, trained on real placement data, evaluates your profile.
    - 🔹 You get a **placement prediction** along with **salary estimate**.
    
    ### 🎯 Why use this tool?
    - 🚀 **No more guessing** – Get data-driven insights on your placement chances.
    - 📊 **Plan your next move** – Improve the skills that matter most to recruiters.
    - 💼 **Ace your job applications** – Stand out by knowing what top companies are looking for.
    
    This isn't just a prediction tool—it's your personal **placement guide**. Ready to take control of your future? Click the button below and let's get started! 🚀
    """
)

if st.button("🚀 Start Prediction"):
    st.switch_page("pages/prediction.py")