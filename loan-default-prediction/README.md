[![GitHub repo](https://img.shields.io/badge/Health_Insurance-Cost_Predictor-blue?logo=github)](https://github.com/Mullaivendan9894/Machine-Learning/tree/master/loan-default-prediction)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://loan-default-classifier.streamlit.app/)


# 🏦 Credit Risk Assessment Model

A machine learning system that predicts loan default probability and generates CIBIL-like credit scores (300-900) with risk classification.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 Risk Prediction | Logistic Regression model with 94% recall for defaults |
| 📊 Credit Scoring | 300-900 score with Poor/Average/Good/Excellent ratings |
| 🖥️ Interactive UI | Streamlit dashboard for loan officers |
| ⚖️ Class Balancing | SMOTE-Tomek for handling imbalanced data |

## 📂 Dataset

**37,500 loan applications** with 32 features across 4 categories:

### 🧑‍💼 Customer Attributes
- Demographics: `age`, `gender`, `marital_status`
- Financials: `income`, `employment_status`, `bank_balance`

### 💰 Loan Details
- `loan_amount`, `tenure_months`, `purpose`, `type`
- `processing_fee`, `net_disbursement`

### 🏦 Credit History
- `delinquent_months`, `total_dpd`, `enquiry_count`
- `credit_utilization_ratio`, `open_accounts`

### 🎯 Target Variable
- `default` (Binary: 0=Paid, 1=Default)

### 🛠️ Engineered Features
| Feature | Formula | Purpose |
|---------|---------|---------|
| Loan-to-Income | `loan_amount / income` | Measures repayment capacity |
| Delinquency Ratio | `(delinquent_months / total_loan_months)*100` | Payment delinquency history |
| Avg DPD | `total_dpd / delinquent_months` | Severity of late payments |

## 🧪 Model Development

### 🔍 Feature Selection
 most important features selected using:
- Weight of Evidence (WOE)
- Information Value (> 0.02)
- Variance Inflation Factor (VIF < 5)

<pre>```python
['age', 'residence_type', 'loan_purpose', 'loan_type',
 'loan_tenure_months', 'number_of_open_accounts',
 'credit_utilization_ratio', 'loan_to_income',
 'delinquent_ratio', 'avg_dpd_per_deliquency']</pre>


 ## 📊 Model Performance Evolution

| Attempt | Technique       | Model               | Accuracy | Default Recall |
|---------|-----------------|---------------------|----------|----------------|
| 1       | Baseline        | Logistic Regression | 96%      | 72%            |
| 2       | Under-sampling  | XGBoost             | 93%      | 94%            |
| 3       | **SMOTE-Tomek** | **Logistic Regression** | **93%**  | **94%**        |

### ✅ Final Model Metrics

- **AUC:** 98.36%  
- **Gini Coefficient:** 96.73%  


#### 📦 Project Structure

<pre>``` health-insurance-cost-predictor/
├── artifacts/                # Saved models and encoders
├── main.py                   # Streamlit application
├── prediction_helper.py      # Prediction functions
├── README.md                 # This file
├── requirements.txt          # Dependencies```</pre>


#### ⚙️ Install Dependencies
<pre> pip install -r requirements.txt </pre>

#### 🚀 Run Streamlit App
<pre> streamlit run app.py </pre>
