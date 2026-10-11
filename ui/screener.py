import streamlit as st
from config.roles import ROLES
from src.trainer import predict
from src.features import score_resume_for_role, get_missing_keywords


def render_screener(trained_models: dict) -> None:
    col_input, col_result = st.columns([1, 1], gap="large")

    with col_input:
        st.markdown("<div class='section-label'>Select Role to Screen For</div>", unsafe_allow_html=True)
        selected_role = st.selectbox("Role", list(ROLES.keys()), label_visibility="collapsed")
        role_info = ROLES[selected_role]
        acc = trained_models[selected_role]["accuracy"]

        st.markdown(f"""
        <div style='margin: 12px 0 18px; display:flex; align-items:center; gap:10px;'>
            <span class='model-tag {role_info["model_class"]}'>{role_info["model_name"]}</span>
            <span style='font-size:0.8rem; color:#9B9B9B;'>Accuracy: {acc*100:.1f}%</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-label'>Paste Resume Text Below</div>", unsafe_allow_html=True)
        resume_input = st.text_area(
            "Resume", height=320,
            placeholder="Paste the full resume text here...",
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)
        screen_btn = st.button("🔍 Screen This Resume", use_container_width=True)

    with col_result:
        st.markdown("<div class='section-label'>Screening Result</div>", unsafe_allow_html=True)

        if screen_btn and resume_input.strip():
            prediction, prob = predict(resume_input, selected_role, trained_models)
            keywords = role_info["keywords"]
            matched_count, matched_kws = score_resume_for_role(resume_input, keywords)
            missed_kws = get_missing_keywords(resume_input, keywords)
            role_label = selected_role.split(" ", 1)[1]

            if prediction == 1:
                st.markdown(f"""
                <div class='result-block result-selected'>
                    <div style='font-size:2rem; margin-bottom:8px;'>🎉</div>
                    <div class='result-title'>Selected!</div>
                    <div class='result-sub'>Qualifies for <strong>{role_label}</strong></div>
                    <div class='score-pill score-pill-selected'>Confidence: {prob*100:.0f}%</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='result-block result-rejected'>
                    <div style='font-size:2rem; margin-bottom:8px;'>❌</div>
                    <div class='result-title'>Not Shortlisted</div>
                    <div class='result-sub'>Does not meet threshold for <strong>{role_label}</strong></div>
                    <div class='score-pill score-pill-rejected'>Mismatch: {(1-prob)*100:.0f}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<div class='section-label'>Matched Keywords</div>", unsafe_allow_html=True)
            if matched_kws:
                chips = "".join([f"<span class='keyword-chip match'>✓ {kw}</span>" for kw in matched_kws[:15]])
                st.markdown(f"<div>{chips}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:#9B9B9B; font-size:0.85rem;'>No role keywords found.</p>", unsafe_allow_html=True)

            if missed_kws:
                st.markdown("<br><div class='section-label'>Missing Keywords (Top 10)</div>", unsafe_allow_html=True)
                chips = "".join([f"<span class='keyword-chip miss'>✗ {kw}</span>" for kw in missed_kws])
                st.markdown(f"<div>{chips}</div>", unsafe_allow_html=True)

            st.markdown(f"""
            <div style='margin-top:18px; padding:14px 18px; background:white; border:1.5px solid #E0D9CE; border-radius:12px;'>
                <div class='section-label'>Keyword Match Score</div>
                <div style='font-family:DM Serif Display,serif; font-size:1.4rem; color:#1C1C1E;'>
                    {matched_count} <span style='font-size:0.9rem; color:#9B9B9B;'>/ {len(keywords)} keywords matched</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif screen_btn:
            st.warning("Please paste a resume to screen.")
        else:
            st.markdown("""
            <div style='margin-top:20px; padding:40px 28px; background:white; border:1.5px dashed #D0C9BE; border-radius:16px; text-align:center;'>
                <div style='font-size:2.5rem; margin-bottom:14px;'>📄</div>
                <div style='font-family:DM Serif Display,serif; font-size:1.3rem; color:#1C1C1E; margin-bottom:6px;'>Awaiting Resume</div>
                <div style='font-size:0.85rem; color:#9B9B9B;'>Select a role, paste resume text, and click Screen.</div>
            </div>
            """, unsafe_allow_html=True)
