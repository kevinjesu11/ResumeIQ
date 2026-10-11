import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

from config.roles import ROLES, ROLE_MODELS, DATA_PATH
from src.preprocessor import clean_text
from src.features import assign_label


@st.cache_resource
def load_and_train(data_path: str = DATA_PATH) -> tuple:
    df = pd.read_csv(data_path)
    df["resume_text"] = df["resume_text"].fillna("")
    df["clean_text"] = df["resume_text"].apply(clean_text)

    trained = {}

    for role_name, role_info in ROLES.items():
        label_col = f"label_{role_info['key']}"
        df[label_col] = df["resume_text"].apply(
            lambda x: assign_label(x, role_info["keywords"])
        )

        labels = df[label_col]
        tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=2000, min_df=1)
        X = tfidf.fit_transform(df["clean_text"])
        y = labels

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42,
            stratify=y if y.nunique() > 1 else None
        )

        clf = ROLE_MODELS[role_name]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        trained[role_name] = {
            "model":            clf,
            "tfidf":            tfidf,
            "accuracy":         accuracy_score(y_test, y_pred),
            "confusion_matrix": confusion_matrix(y_test, y_pred),
            "precision":        precision_score(y_test, y_pred, zero_division=0),
            "recall":           recall_score(y_test, y_pred, zero_division=0),
            "f1":               f1_score(y_test, y_pred, zero_division=0),
            "label_counts":     labels.value_counts().to_dict(),
        }

    return trained, df


def predict(resume_text: str, role_name: str, trained_models: dict) -> tuple:
    role_data = trained_models[role_name]
    model = role_data["model"]
    tfidf = role_data["tfidf"]

    cleaned = clean_text(resume_text)
    vec = tfidf.transform([cleaned])
    prediction = model.predict(vec)[0]
    prob = (
        model.predict_proba(vec)[0][1]
        if hasattr(model, "predict_proba")
        else (0.85 if prediction == 1 else 0.25)
    )
    return int(prediction), float(prob)
