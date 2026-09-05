# Credit Risk & Loan Default Prediction with Explainability

A machine learning system that predicts the probability a loan applicant will default, and explains *why* using SHAP - built as a Streamlit web app backed by a FastAPI service.

## Live Demo
- App: []
- API docs: [YOUR_RENDER_URL_HERE]/docs

## Problem Statement
Lenders need to assess the risk of a loan applicant defaulting - but a black-box "yes/no" isn't enough for real decision-making or regulatory transparency. This project predicts default probability and explains which factors drove each prediction.

## Dataset
- Source: Lending Club Loan Data (Kaggle)
- Size: ~1.3 million loans with a known final outcome
- Target definition: Loans were filtered to only Fully Paid (repaid, target = 0) and Charged Off (defaulted, target = 1). Loans still Current, Late, or In Grace Period were excluded, since their outcome isn't known yet - including them would leak future information into the model.

## Approach
1. Loaded and cleaned ~1.3M rows, selecting 15+ features known at application time
2. Encoded categorical features, handled missing values, split into train/test sets (stratified 80/20)
3. Trained and compared four models
4. Tuned the best model with RandomizedSearchCV
5. Added SHAP explainability to break down individual predictions
6. Built a FastAPI backend serving predictions plus explanations
7. Built a Streamlit frontend for interactive use
8. Deployed both publicly (Render plus Streamlit Community Cloud)

## Model Comparison

| Model | ROC-AUC |
|---|---|
| Logistic Regression (baseline) | 0.676 |
| Random Forest | 0.699 |
| LightGBM | 0.713 |
| XGBoost (tuned, final) | 0.712 |

Final model: XGBoost (n_estimators=100, max_depth=5, learning_rate=0.1)
- ROC-AUC: 0.712
- Recall (default class): 0.67
- Precision (default class): 0.32

## Explainability
Each prediction is accompanied by a SHAP-based breakdown of the top 5 features that pushed that specific applicant's risk score up or down.

## Screenshots
[Add screenshots of your Streamlit app here]

## Tech Stack
- Modeling: pandas, scikit-learn, XGBoost, SHAP
- Backend: FastAPI
- Frontend: Streamlit
- Deployment: Render (API), Streamlit Community Cloud (app)

## Running Locally

1. Clone the repo and set up a virtual environment:
   git clone https://github.com/Sowmya-bandaru/credit-risk-prediction.git
   cd credit-risk-prediction
   python -m venv venv
   venv\\Scripts\\activate
   pip install -r requirements.txt

2. Download the Lending Club dataset from Kaggle and place it in data/raw/.
3. Run the notebooks in notebooks/ in order (00 to 03) to reproduce preprocessing, modeling, and explainability.
4. Start the API:
   cd api
   uvicorn main:app --reload

5. In a separate terminal, start the app:
   cd app
   streamlit run app.py

## Author
[Sowmya]
