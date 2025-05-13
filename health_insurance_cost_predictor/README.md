[![GitHub repo](https://img.shields.io/badge/Health_Insurance-Cost_Predictor-blue?logo=github)](https://github.com/Mullaivendan9894/Machine-Learning/tree/master/health_insurance_cost_predictor)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://premium-health-insurance-cost-predictor.streamlit.app/)


## 💼 Health Insurance Cost Predictor

A Machine Learning-powered web application that predicts annual health insurance premium amounts based on user-specific personal and health details. This project employs Linear Regression and XGBoost Regressor models, combined with advanced feature engineering and age-based segmentation, to achieve high prediction accuracy.

### 📌 Project Overview

The rising cost of healthcare has made health insurance an essential component of financial planning. However, premiums vary significantly based on several factors. This project helps predict the Annual Premium Amount for users based on attributes like age, gender, income, BMI category, medical history, and more.

**Built with:**

* Python
* Pandas, Scikit-learn, XGBoost
* Streamlit (for UI)
* Joblib (for model persistence)

### 📊 Dataset Features

The dataset used includes the following attributes:

* Age
* Gender
* Region
* Marital\_status
* Number Of Dependants
* BMI\_Category
* Smoking\_Status
* Employment\_Status
* Income\_Level
* Income\_Lakhs
* Medical History
* Insurance\_Plan
* Annual\_Premium\_Amount (Target)

### 🧠 Feature Engineering & Modeling Insights

#### 🔍 EDA & Multicollinearity Check

* Performed extensive Exploratory Data Analysis.
* Conducted Variance Inflation Factor (VIF) analysis to detect multicollinearity.
* Dropped `Income_Level` due to high correlation with other features.

#### 🏗️ Model Training

* Trained both Linear Regression and XGBoost Regressor models.
* Initially observed high error margins, especially in predictions for younger individuals.

#### ⚖️ Error Analysis & Optimization

* Segmented the dataset into two age groups:
    * Group 1: Users aged ≤ 25
    * Group 2: Users aged > 25
* Introduced a new feature `genetical_risk` to improve prediction accuracy.
* Applied age-specific models:
    * **Linear Regression for Group 1:** → 98.8% Accuracy
    * **XGBoost for Group 2:** → 99.7% Accuracy

#### 📦 Project Structure

<pre>``` health-insurance-cost-predictor/
├── artifacts/                # Saved models and encoders
├── app.py                    # Streamlit application
├── prediction_helper.py      # Prediction functions
├── README.md                 # This file
├── requirements.txt          # Dependencies```</pre>

#### ⚙️ Install Dependencies
<pre> pip install -r requirements.txt </pre>

#### 🚀 Run Streamlit App
<pre> streamlit run app.py </pre>
