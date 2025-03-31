import streamlit as st
import pdfplumber
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sidebar

load_dotenv()
genai.configure(api_key=AIzaSyCaNfYJCTRIJR5ppjDxk1HFPzqUD1M7ci4)

def extract_text_from_pdf(uploaded_file):
    """Extracts text from uploaded PDF using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or "" 
    except Exception as e:
        st.error(f"⚠ Error reading PDF: {e}")
        return None
    return text

def parse_resume_with_gemini(text):
    """Uses Gemini AI to extract structured resume information."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    prompt = f"""
    You are an AI-powered resume parser. Extract key details from the following resume text:

    --- RESUME TEXT ---
    {text}

    TASKS:
    - Extract the candidate's full name.
    - Extract email and phone number.
    - Identify educational qualifications (Degree, Institution, Year).
    - Extract technical skills (list).
    - Identify projects (if available).
    - Predict the best career path based on skills.
    - Suggest recommended job roles.
    - Predict an expected salary range.

    OUTPUT FORMAT:
    **📌 Name:** [Candidate Name]
    
    **📧 Email:** [email@example.com]
    
    **📞 Phone:** [+91XXXXXXXXXX]
    
    **🎓 Education:**
    - [Degree] from [Institution] (Year)
    - [Degree] from [Institution] (Year)
    
    **🛠 Technical Skills:**
    - Python, SQL, Machine Learning, ReactJS
    
    **📂 Projects:**
    - **Project 1:** [Short Description]
    - **Project 2:** [Short Description]
    
    **🚀 Career Prediction:** [Predicted Career Path]
    **💼 Recommended Roles:** Data Scientist, AI Engineer, Software Developer
    **💰 Predicted Salary:** ₹5,00,000 - ₹7,00,000 per year
    """

    response = model.generate_content(prompt)
    return response.text 

def analyze_with_gemini(resume_text, jd_text):
    """Uses Gemini AI to compare resume and JD for ATS-style matching."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    prompt = f"""
    You are an AI-powered ATS (Applicant Tracking System). Analyze the following resume against the given job description.

    --- RESUME TEXT ---
    {resume_text}

    --- JOB DESCRIPTION ---
    {jd_text}

    TASKS:
    - Provide a match percentage score.
    - Identify missing or weak skills.
    - Suggest improvements in bullet points.

    OUTPUT FORMAT:
    **📊 Match Score:** 85%
    
    **🔍 Missing Skills:**
    - Cloud Computing
    - DevOps
    - CI/CD
    
    **📝 Improvement Suggestions:**
    - Add more details about project experience.
    - Include a dedicated section for certifications.
    - Improve resume formatting for better ATS readability.
    """

    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="AI Resume + ATS", layout="wide")

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

st.title("📄 AI Resume Analyzer with Job Matching")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
jd_input = st.text_area("Paste the Job Description below 👇", height=250)

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    if text:
        st.subheader("📋 Extracted Resume Details")
        resume_analysis = parse_resume_with_gemini(text)
        st.markdown(resume_analysis)

        if jd_input:
            with st.spinner("🧠 Analyzing Resume vs JD using our model..."):
                ats_feedback = analyze_with_gemini(text, jd_input)

            st.subheader("📊 JD Comparison & Suggestions")
            st.markdown(ats_feedback)
