import streamlit as st

def load_sidebar():
    with st.sidebar:
        st.markdown("""
        <style>
        .sidebar-title {
            font-size: 24px;
            font-weight: bold;
            color: #FFA500;
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .sidebar-button {
            display: flex;
            align-items: center;
            background: #FFA500;
            color: white;
            padding: 12px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 12px;
            text-decoration: none;
            transition: background 0.3s;
        }
        .sidebar-button:hover {
            background: #FF8C00;
        }
        .sidebar-button img {
            width: 24px;
            height: 24px;
            margin-right: 10px;
        }
        [data-testid="stSidebarNav"] { 
            display: none; 
        }
        </style>

        <div class='sidebar-title'>🔮 Navigation</div>
        <a class='sidebar-button' href='/'>
            <img src='https://img.icons8.com/fluency/48/home.png'/> Home
        </a>
        <a class='sidebar-button' href='/prediction'>
            <img src='https://img.icons8.com/fluency/48/combo-chart.png'/> Prediction
        </a>
        <a class='sidebar-button' href='/ats'>
            <img src='https://img.icons8.com/fluency/48/document.png'/> ATS Analysis
        </a>
        """, unsafe_allow_html=True)
