# Intelligent Bug Triage & Fix-Time Prediction

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