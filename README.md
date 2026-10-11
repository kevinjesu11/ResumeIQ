# 📋 ResumeIQ — Smart Resume Screener

An AI-powered resume screening system using NLP + 4 different ML models across 4 job roles.

---

## 🗂️ Project Structure

```
ResumeIQ/
│
├── app.py                  ← Main entry point (run this)
├── requirements.txt        ← Python dependencies
├── README.md
│
├── config/
│   ├── __init__.py
│   └── roles.py            ← Role definitions, keywords, model configs
│
├── src/
│   ├── __init__.py
│   ├── preprocessor.py     ← Text cleaning (regex + stopwords)
│   ├── features.py         ← Keyword scoring & label assignment
│   └── trainer.py          ← Model training, evaluation & prediction
│
├── ui/
│   ├── __init__.py
│   ├── styles.py           ← All CSS styling
│   ├── sidebar.py          ← Sidebar component
│   ├── screener.py         ← Resume screening UI
│   └── performance.py      ← Confusion matrices & metrics dashboard
│
├── data/
│   └── resumes.csv         ← Training dataset (224 resumes)
│
└── notebooks/
    └── eda.ipynb           ← Exploratory Data Analysis (optional)
```

---

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🎯 Roles & ML Models

| Role | Model | Why |
|---|---|---|
| ☕ Java Developer | Logistic Regression | Effective for high-dimensional text |
| 📊 Business Analyst | Decision Tree | Interpretable, keyword-driven |
| 🗂️ Project Manager | SVM (Linear) | Strong in sparse feature spaces |
| ⚙️ DevOps Engineer | Random Forest | Handles noisy keyword combos |

---

## 🧠 ML Pipeline

```
Raw Resume Text
      ↓
  Preprocessing       (regex clean + stopword removal)
      ↓
  TF-IDF Vectors      (bigrams, 2000 features per role)
      ↓
  Role Labeling       (keyword threshold = 8 matches)
      ↓
  Model Training      (separate model per role)
      ↓
  Evaluation          (accuracy, F1, precision, recall, confusion matrix)
      ↓
  Prediction          (shortlisted ✅ / not shortlisted ❌ + confidence %)
```

---

## 📊 Features

- Paste any resume → instant prediction with confidence score
- Matched keywords shown in green, missing in red
- Confusion matrix for all 4 models
- Accuracy / F1 / Precision / Recall per model
- Dataset overview with shortlist rates

---

## 📦 Dataset

- 224 real resumes from `resumes.csv`
- Columns used: `resume_text`
- Labels auto-generated via keyword matching per role
