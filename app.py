import numpy as np
import streamlit as st

from config.roles import ROLES, DATA_PATH
from src.trainer import load_and_train
from ui.styles import CSS
from ui.sidebar import render_sidebar
from ui.screener import render_screener
from ui.performance import render_performance_dashboard, render_dataset_overview

st.set_page_config(
    page_title="ResumeIQ — Smart Screener",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(CSS, unsafe_allow_html=True)

with st.spinner("🔄 Training models on your resume dataset..."):
    trained_models, df = load_and_train(DATA_PATH)

render_sidebar(trained_models, total_resumes=len(df))

st.markdown("""
<div class='hero'>
    <div class='hero-left'>
        <h1>Resume<span>IQ</span></h1>
        <div class='hero-tagline'>AI-Powered Smart Resume Screener · 4 Roles · 4 ML Models</div>
    </div>
    <div class='hero-badge'>TF-IDF + ML</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='role-grid'>
    <div class='role-card java'>
        <div class='role-icon'>☕</div>
        <div class='role-name'>Java Developer</div>
        <div class='role-model'>Logistic Regression</div>
    </div>
    <div class='role-card ba'>
        <div class='role-icon'>📊</div>
        <div class='role-name'>Business Analyst</div>
        <div class='role-model'>Decision Tree</div>
    </div>
    <div class='role-card pm'>
        <div class='role-icon'>🗂️</div>
        <div class='role-name'>Project Manager</div>
        <div class='role-model'>Support Vector Machine</div>
    </div>
    <div class='role-card devops'>
        <div class='role-icon'>⚙️</div>
        <div class='role-name'>DevOps Engineer</div>
        <div class='role-model'>Random Forest</div>
    </div>
</div>
""", unsafe_allow_html=True)

avg_acc = np.mean([trained_models[r]["accuracy"] for r in ROLES]) * 100

st.markdown(f"""
<div class='stat-row'>
    <div class='stat-box'>
        <div class='stat-num'>{len(df)}</div>
        <div class='stat-desc'>Resumes in Training Set</div>
    </div>
    <div class='stat-box'>
        <div class='stat-num'>{avg_acc:.0f}%</div>
        <div class='stat-desc'>Average Model Accuracy</div>
    </div>
    <div class='stat-box'>
        <div class='stat-num'>{len(ROLES)}</div>
        <div class='stat-desc'>Roles with Unique ML Models</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

render_screener(trained_models)
render_performance_dashboard(trained_models)
render_dataset_overview(trained_models)

st.markdown("""
<div style='text-align:center; padding:2rem 0 0.5rem; font-size:0.78rem; color:#C0B9AD; letter-spacing:0.06em;'>
    RESUMEIQ · TF-IDF · SCIKIT-LEARN · STREAMLIT
</div>
""", unsafe_allow_html=True)
