# Intelligent Bug Triage & Fix-Time Prediction

## My Motive
This project is a part of my self-studies, where I challenge myself to implement an end-to-end machine learning pipeline; from raw, multi-source data ingestion and rigorous cleaning to advanced feature engineering and the deployment of multivariate statistical and machine learning models (PCA, LDA, linear and logistic regression, CART, k‑nearest neighbors, and neural networks)— to solve a real-world software engineering problem: intelligent bug triage and fix‑time prediction. It reflects my hands-on commitment to mastering the exact skills required in data-driven technology roles at companies like IBM, Deloitte, Oracle, and SAP.

## Phase 1: Setup and Data Exploration

### Objective
Predict bug fix times and classify bug severity using structured and unstructured data from the Mozilla Bugzilla repository. This project demonstrates an end‑to‑end ML pipeline tailored for enterprise software engineering teams.

### Dataset
Mozilla Bugzilla public dataset (source: Kaggle / MSR challenge).
Contains:
- `bugs.csv`: metadata (severity, priority, product, timestamps…)
- `comments.csv`: unstructured text (bug descriptions, user comments)
- `attachments.csv`, `history.csv`: relational data for developer activity

### Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```
