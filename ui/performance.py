import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from config.roles import ROLES


def render_performance_dashboard(trained_models: dict) -> None:
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='margin-bottom:20px;'>
        <div class='section-label'>Model Performance Dashboard</div>
        <div style='font-family:DM Serif Display,serif; font-size:2rem; color:#1C1C1E; margin-top:4px;'>
            Accuracy, Metrics &amp; Confusion Matrices
        </div>
    </div>
    """, unsafe_allow_html=True)

    perf_cols = st.columns(4)
    for i, (role_name, role_info) in enumerate(ROLES.items()):
        data = trained_models[role_name]
        with perf_cols[i]:
            st.markdown(f"""
            <div style='background:white; border:1.5px solid #E0D9CE; border-radius:14px; padding:18px; margin-bottom:16px;'>
                <div style='font-size:1.2rem; margin-bottom:4px;'>{role_name.split()[0]}</div>
                <div style='font-weight:600; font-size:0.85rem; color:#1C1C1E;'>{role_name.split(" ",1)[1]}</div>
                <span class='model-tag {role_info["model_class"]}' style='margin:8px 0; display:inline-block;'>
                    {role_info["model_name"]}
                </span>
                <div style='display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:10px;'>
                    <div style='background:#F5F0E8; border-radius:8px; padding:10px; text-align:center;'>
                        <div style='font-family:DM Serif Display,serif; font-size:1.4rem; color:#1C1C1E;'>{data["accuracy"]*100:.1f}%</div>
                        <div style='font-size:0.68rem; color:#9B9B9B; text-transform:uppercase; letter-spacing:0.05em;'>Accuracy</div>
                    </div>
                    <div style='background:#F5F0E8; border-radius:8px; padding:10px; text-align:center;'>
                        <div style='font-family:DM Serif Display,serif; font-size:1.4rem; color:#1C1C1E;'>{data["f1"]*100:.1f}%</div>
                        <div style='font-size:0.68rem; color:#9B9B9B; text-transform:uppercase; letter-spacing:0.05em;'>F1 Score</div>
                    </div>
                    <div style='background:#F5F0E8; border-radius:8px; padding:10px; text-align:center;'>
                        <div style='font-family:DM Serif Display,serif; font-size:1.4rem; color:#1C1C1E;'>{data["precision"]*100:.1f}%</div>
                        <div style='font-size:0.68rem; color:#9B9B9B; text-transform:uppercase; letter-spacing:0.05em;'>Precision</div>
                    </div>
                    <div style='background:#F5F0E8; border-radius:8px; padding:10px; text-align:center;'>
                        <div style='font-family:DM Serif Display,serif; font-size:1.4rem; color:#1C1C1E;'>{data["recall"]*100:.1f}%</div>
                        <div style='font-size:0.68rem; color:#9B9B9B; text-transform:uppercase; letter-spacing:0.05em;'>Recall</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:8px;'><div class='section-label'>Confusion Matrices — All 4 Models</div></div>", unsafe_allow_html=True)

    cm_cols = st.columns(4)
    for i, (role_name, role_info) in enumerate(ROLES.items()):
        data = trained_models[role_name]
        cm   = data["confusion_matrix"]

        with cm_cols[i]:
            fig, ax = plt.subplots(figsize=(3.2, 2.8))
            fig.patch.set_facecolor("#FFFFFF")
            ax.set_facecolor("#FFFFFF")

            sns.heatmap(
                cm, annot=True, fmt="d", cmap=plt.cm.RdYlGn,
                xticklabels=["Rejected", "Selected"],
                yticklabels=["Rejected", "Selected"],
                ax=ax, cbar=False, linewidths=1, linecolor="#F5F0E8",
                annot_kws={"size": 14, "weight": "bold", "color": "#1C1C1E"}
            )
            ax.set_xlabel("Predicted", fontsize=8, color="#6B6B6B", labelpad=6)
            ax.set_ylabel("Actual",    fontsize=8, color="#6B6B6B", labelpad=6)
            ax.tick_params(colors="#6B6B6B", labelsize=7.5)
            ax.set_title(
                f"{role_name.split(' ',1)[1]}\n{role_info['model_name']}",
                fontsize=8.5, color="#1C1C1E", fontweight="bold", pad=10
            )
            for spine in ax.spines.values():
                spine.set_edgecolor("#E0D9CE")
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

            tn = cm[0][0] if cm.shape == (2, 2) else 0
            fp = cm[0][1] if cm.shape == (2, 2) else 0
            fn = cm[1][0] if cm.shape == (2, 2) else 0
            tp = cm[1][1] if cm.shape == (2, 2) else 0

            st.markdown(f"""
            <div style='background:white; border:1.5px solid #E0D9CE; border-radius:10px; padding:12px; font-size:0.75rem; margin-top:4px;'>
                <div style='display:grid; grid-template-columns:1fr 1fr; gap:4px;'>
                    <div style='color:#166534;'>✅ True Pos: <b>{tp}</b></div>
                    <div style='color:#991B1B;'>❌ False Pos: <b>{fp}</b></div>
                    <div style='color:#065F46;'>✅ True Neg: <b>{tn}</b></div>
                    <div style='color:#C8541A;'>⚠️ False Neg: <b>{fn}</b></div>
                </div>
            </div>
            """, unsafe_allow_html=True)


def render_dataset_overview(trained_models: dict) -> None:
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Dataset Overview — Shortlisted per Role</div>", unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (role_name, role_info) in enumerate(ROLES.items()):
        counts      = trained_models[role_name]["label_counts"]
        shortlisted = counts.get(1, 0)
        total       = shortlisted + counts.get(0, 0)
        pct         = (shortlisted / total * 100) if total > 0 else 0
        acc         = trained_models[role_name]["accuracy"]

        with cols[i]:
            st.markdown(f"""
            <div style='background:white; border:1.5px solid #E0D9CE; border-radius:14px; padding:20px 18px;'>
                <div style='font-size:1.4rem; margin-bottom:6px;'>{role_name.split()[0]}</div>
                <div style='font-weight:600; font-size:0.9rem; color:#1C1C1E; margin-bottom:12px;'>{role_name.split(" ",1)[1]}</div>
                <div style='font-family:DM Serif Display,serif; font-size:2rem; color:#1C1C1E;'>{shortlisted}</div>
                <div style='font-size:0.78rem; color:#9B9B9B; margin-bottom:12px;'>shortlisted of {total}</div>
                <div style='background:#F0EBE1; border-radius:100px; height:6px; overflow:hidden;'>
                    <div style='background:{role_info["color"]}; height:100%; width:{pct:.0f}%; border-radius:100px;'></div>
                </div>
                <div style='font-size:0.72rem; color:#9B9B9B; margin-top:6px;'>
                    {pct:.0f}% shortlist rate &nbsp;·&nbsp; {acc*100:.0f}% acc
                </div>
                <span class='model-tag {role_info["model_class"]}' style='margin-top:10px; display:inline-block;'>
                    {role_info["model_name"]}
                </span>
            </div>
            """, unsafe_allow_html=True)
