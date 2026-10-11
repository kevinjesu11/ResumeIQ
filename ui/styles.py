CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, .stApp {
    background-color: #F5F0E8;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: #1C1C1E !important;
    border-right: none;
}
[data-testid="stSidebar"] * { color: #E8E0D0 !important; }

.block-container { padding: 2.5rem 3rem; max-width: 1200px; }

.hero {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    border-bottom: 2px solid #1C1C1E;
    padding-bottom: 1.5rem;
    margin-bottom: 2.5rem;
}
.hero-left h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 3.8rem;
    color: #1C1C1E;
    line-height: 1.0;
    letter-spacing: -1px;
}
.hero-left h1 span { color: #C8541A; font-style: italic; }
.hero-tagline {
    font-size: 0.9rem; color: #6B6B6B; margin-top: 10px;
    letter-spacing: 0.05em; text-transform: uppercase;
}
.hero-badge {
    background: #1C1C1E; color: #F5F0E8;
    padding: 10px 22px; border-radius: 100px;
    font-size: 0.8rem; letter-spacing: 0.08em;
    text-transform: uppercase; font-weight: 500;
}

.role-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 14px; margin-bottom: 2.5rem;
}
.role-card {
    background: white; border: 1.5px solid #E0D9CE;
    border-radius: 14px; padding: 20px 18px;
    position: relative; overflow: hidden;
}
.role-card::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    border-radius: 14px 14px 0 0;
}
.role-card.java::before  { background: #3B82F6; }
.role-card.ba::before    { background: #10B981; }
.role-card.pm::before    { background: #F59E0B; }
.role-card.devops::before{ background: #EF4444; }
.role-icon  { font-size: 1.8rem; margin-bottom: 10px; }
.role-name  { font-size: 0.95rem; font-weight: 600; color: #1C1C1E; }
.role-model { font-size: 0.75rem; color: #9B9B9B; margin-top: 4px; }

.section-label {
    font-size: 0.75rem; font-weight: 600;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: #9B9B9B; margin-bottom: 10px;
}

.result-block { border-radius: 16px; padding: 28px 32px; margin-top: 20px; }
.result-selected { background: #1C1C1E; border: none; }
.result-rejected { background: #FFF5F0; border: 2px solid #FECACA; }
.result-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem; margin-bottom: 6px;
}
.result-selected .result-title { color: #F5F0E8; }
.result-rejected .result-title { color: #C8541A; }
.result-sub { font-size: 0.9rem; opacity: 0.65; }
.result-selected .result-sub { color: #E8E0D0; }
.result-rejected .result-sub { color: #6B6B6B; }

.score-pill {
    display: inline-block; padding: 6px 18px;
    border-radius: 100px; font-size: 0.85rem;
    font-weight: 600; margin-top: 14px;
}
.score-pill-selected { background: #C8541A; color: white; }
.score-pill-rejected { background: #FEE2E2; color: #C8541A; }

.keyword-chip {
    display: inline-block; background: #F0EBE1;
    border: 1px solid #DDD5C7; color: #3A3A3A;
    border-radius: 100px; padding: 5px 14px;
    font-size: 0.78rem; margin: 3px; font-weight: 500;
}
.keyword-chip.match { background: #DCFCE7; border-color: #86EFAC; color: #166534; }
.keyword-chip.miss  { background: #FEF2F2; border-color: #FECACA; color: #991B1B; }

.stat-row {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 14px; margin-bottom: 2rem;
}
.stat-box {
    background: white; border: 1.5px solid #E0D9CE;
    border-radius: 12px; padding: 18px 22px;
}
.stat-num { font-family: 'DM Serif Display', serif; font-size: 2rem; color: #1C1C1E; }
.stat-desc { font-size: 0.8rem; color: #9B9B9B; margin-top: 2px; }

.stTextArea textarea {
    background: white !important; border: 1.5px solid #E0D9CE !important;
    border-radius: 12px !important; font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important; color: #1C1C1E !important; padding: 14px !important;
}

div.stButton > button {
    background: #1C1C1E !important; color: #F5F0E8 !important;
    border: none !important; border-radius: 10px !important;
    padding: 12px 0 !important; font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important; font-weight: 600 !important;
    letter-spacing: 0.04em !important; width: 100% !important;
}
div.stButton > button:hover { background: #C8541A !important; }

.stSelectbox > div > div {
    background: white !important; border: 1.5px solid #E0D9CE !important;
    border-radius: 10px !important; color: #1C1C1E !important;
}

.divider { height: 1.5px; background: #E0D9CE; margin: 2rem 0; }

.model-tag {
    display: inline-block; padding: 3px 12px; border-radius: 100px;
    font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.06em; text-transform: uppercase;
}
.model-java   { background: #DBEAFE; color: #1D4ED8; }
.model-ba     { background: #D1FAE5; color: #065F46; }
.model-pm     { background: #FEF3C7; color: #92400E; }
.model-devops { background: #FEE2E2; color: #991B1B; }

.sidebar-role-item { padding: 12px 0; border-bottom: 1px solid #333; }
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #2A2A2C !important; border: 1px solid #444 !important; color: #E8E0D0 !important;
}
</style>
"""
