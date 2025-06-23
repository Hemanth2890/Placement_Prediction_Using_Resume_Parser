# Placement_Prediction_Using_Resume_Parser
The AI Resume Analyzer &amp; ATS Matcher extracts key details from resumes using pdfplumber and analyzes them with Google Gemini AI to predict job roles, salary, and match scores against job descriptions. Built with Python, it helps users optimize their resumes for better ATS compatibility and job success. 

# How to Run the Project

 1. Clone the Repository
Open terminal (or Git Bash on Windows) and run:

git clone https://github.com/Hemanth2890/Placement_Prediction_Using_Resume_Parser.git
cd Placement_Prediction_Using_Resume_Parser

 2. Set Up a Virtual Environment 

python3 -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows

 3. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt

 4. Set Your Gemini API Key
This project uses Google Gemini API (via google.generativeai). You need to set your API key:

On Linux/macOS:
export GOOGLE_API_KEY="your-api-key-here"

On Windows (Command Prompt):
set GOOGLE_API_KEY=your-api-key-here

 5. Prepare Your Resume File
Place a sample resume PDF in the appropriate folder (e.g., uploads or wherever your code reads from).
Update text = extract_text_from_resume(filepath) accordingly if needed.

 6. Run the Application
If you are using Streamlit, run:

streamlit run app.py

If you're running a CLI-based script (like ats.py), run:

python pages/ats.py

 Test Prompt
Once you’re prompted to input a job description, enter something like:

Data Scientist with experience in machine learning, deep learning, and model deployment using AWS and Docker.
You should receive ATS feedback and suggestions in the console.
