# Census Income Classification

## 📌 Project Overview
This project aims to classify individuals based on their annual income using the **1994 U.S. Census dataset**. The goal is to predict whether an individual's income exceeds **$50,000 per year**, leveraging various **machine learning models** and **feature engineering techniques**.

## 📂 Dataset Information
- **Source**: Extracted from the 1994 U.S. Census database.
- **Total Samples**: 48,842
- **Total Features**: 14 (excluding target variable)
- **Target Variable**: `income` (Binary classification: `<=50K` or `>50K`)

### 🔹 Feature Types:
#### **Numerical Features**:
- `age`, `fnlwgt`, `educational-num`, `capital-gain`, `capital-loss`, `hours-per-week`

#### **Categorical Features**:
- `workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `gender`, `native-country`

## 🚀 Project Pipeline
### **1️⃣ Data Preprocessing**
✔ Handling missing values (mode for categorical, median for numerical)
✔ Removing duplicate rows
✔ Handling outliers using Z-score method
✔ Basic feature engineering:
   - Created `capital-net` (capital-gain - capital-loss)
   - Binned `age` into age groups
   - Simplified `native-country` into `US` vs. `Non-US`

### **2️⃣ Exploratory Data Analysis (EDA)**
✔ Summary statistics for numerical and categorical variables
✔ Data visualization: histograms, count plots, box plots
✔ Hypothesis testing (Chi-square test, t-test) to analyze relationships
✔ Class imbalance check

### **3️⃣ Feature Engineering & Encoding**
✔ Dropped redundant features (`fnlwgt`)
✔ Ordinal encoding for ordered categories (`education`, `age_group`)
✔ Label encoding for categorical variables
✔ Standardization of numerical features

### **4️⃣ Handling Class Imbalance**
✔ Applied **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the dataset

### **5️⃣ Feature Selection**
✔ Used **Random Forest** & **Recursive Feature Elimination (RFE)** to select top features
✔ Retained **10 most important features** for model training

### **6️⃣ Model Building & Evaluation**
Multiple machine learning models were trained and evaluated:
| Model | Accuracy | Precision | Recall |
|--------|----------|-----------|--------|
| **Logistic Regression** | 71.87% | 81.14% | 71.87% |
| **Decision Tree Classifier** | 80.35% | 82.99% | 80.35% |
| **Random Forest Classifier** | 81.48% | 84.09% | 81.48% |
| **Gradient Boosting Classifier** | 80.70% | 85.92% | 80.70% |
| **XGBoost Classifier** | **81.90%** | **85.88%** | **81.90%** |
| **XGB_RF Classifier** | 77.39% | 85.80% | 77.39% |

### **7️⃣ Hyperparameter Tuning**
✔ **GridSearchCV** used to fine-tune the XGBoost model
✔ Best parameters found:
   ```json
   {'colsample_bytree': 1.0, 'gamma': 0, 'learning_rate': 0.2, 'max_depth': 7, 'min_child_weight': 1, 'n_estimators': 200, 'subsample': 0.8}
   ```
✔ **Final XGBoost Model Performance:**
   - **Accuracy:** 81.96%
   - **Precision:** 85.60%
   - **Recall:** 81.96%

## 📌 Conclusion
- The **XGBoost Classifier** performed the best with **81.96% accuracy** after hyperparameter tuning.
- The project successfully tackled challenges like **class imbalance** and **feature selection**, leading to improved model performance.
- Future improvements:
  - Further optimize model performance (e.g., boosting techniques, deep learning)
  - Deploy the model using Flask/Streamlit
  - Experiment with additional feature engineering strategies


