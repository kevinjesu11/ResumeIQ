import streamlit as st
from config.roles import ROLES


def render_sidebar(trained_models: dict, total_resumes: int) -> None:
    with st.sidebar:
        st.markdown("## 📋 ResumeIQ")
        st.markdown("---")
        st.markdown("### Role Models")

        for role_name, role_info in ROLES.items():
            acc    = trained_models[role_name]["accuracy"]
            counts = trained_models[role_name]["label_counts"]
            shortlisted = counts.get(1, 0)
            total       = sum(counts.values())

            st.markdown(f"""
            <div class='sidebar-role-item'>
                <div style='font-weight:600; font-size:0.9rem;'>{role_name}</div>
                <div style='font-size:0.78rem; color:#aaa; margin-top:3px;'>{role_info['model_name']}</div>
                <div style='font-size:0.78rem; color:#aaa; margin-top:2px;'>
                    Accuracy: {acc*100:.1f}% &nbsp;|&nbsp; {shortlisted}/{total} shortlisted
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Dataset Info")
        st.markdown(f"""
        <div style='font-size:0.82rem; color:#aaa; line-height:1.8;'>
            📁 Total Resumes: {total_resumes}<br>
            🔤 Text Cleaning: Regex + Stopwords<br>
            🧠 Vectorizer: TF-IDF (bigrams)<br>
            🔬 Models: LR · DT · SVM · RF
        </div>
        """, unsafe_allow_html=True)
