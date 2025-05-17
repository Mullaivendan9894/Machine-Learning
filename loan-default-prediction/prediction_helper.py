import pandas as pd
import numpy as np
import joblib
from joblib import dump
import os
from pathlib import Path

# Get the current directory path where the script is located
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
artifacts_path = current_dir / "artifacts"  # Path to artifacts directory

# Load pre-trained models and encoders from artifacts
model_data = joblib.load(artifacts_path/"model_data.joblib")  # Contains model, scaler, and feature info
model = model_data["model"]
ohe_loan_purpose = joblib.load(artifacts_path/"ohe_loan_purpose.joblib")  # One-hot encoder for loan purpose
ohe_loan_type = joblib.load(artifacts_path/"ohe_loan_type.joblib")  # One-hot encoder for loan type
ohe_resi_type = joblib.load(artifacts_path/"ohe_residence_type.joblib")  # One-hot encoder for residence type


def credit_risk_classification(input_data):
    """
    Predicts credit risk based on applicant information.
    Args:
        input_data (dict): Dictionary containing applicant's financial and personal details    
    Returns:
        tuple: (default_probability, credit_score, rating)
            - default_probability: Probability of default (0-1)
            - credit_score: Calculated credit score (300-900)
            - rating: Textual rating (Poor/Average/Good/Excellent)
    """


    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Feature engineering: Create derived features
    input_df["loan_to_income"] = input_df["loan_amount"] / input_df["income"]  # Debt-to-income ratio
    input_df["delinquent_ratio"] = input_data["delinquent_ratio"]  # Percentage of delinquent payments
    input_df["avg_dpd_per_deliquency"] = input_data["avg_dpd_per_deliquency"]  # Average days past due

    # One-hot encode categorical features
    resi_type_df = pd.DataFrame(
        ohe_resi_type.transform(input_df[["residence_type"]]),
        columns=ohe_resi_type.get_feature_names_out(["residence_type"])
    )
    loan_purpose_df = pd.DataFrame(
        ohe_loan_purpose.transform(input_df[["loan_purpose"]]),
        columns=ohe_loan_purpose.get_feature_names_out(['loan_purpose'])
    )
    loan_type_df = pd.DataFrame(
        ohe_loan_type.transform(input_df[["loan_type"]]),
        columns=ohe_loan_type.get_feature_names_out(["loan_type"])
    )

    # Prepare data for concatenation
    input_df_rest = input_df.drop(["residence_type", "loan_purpose", "loan_type"], axis=1)
    input_df_rest = input_df_rest.reset_index(drop=True)
    loan_purpose_df = loan_purpose_df.reset_index(drop=True)
    loan_type_df = loan_type_df.reset_index(drop=True)

    # Combine all features
    input_df = pd.concat([input_df_rest, resi_type_df, loan_purpose_df, loan_type_df], axis=1)

    # Handle missing columns that were present during training
    cols_to_add = set(model_data["cols_to_scale"]) - set(input_df.columns)
    cols_to_drop = []
    for col in cols_to_add:
        input_df[col] = 0  # Add missing columns with default value 0
        cols_to_drop.append(col)  # Track columns to drop later

    # Scale numerical features using the pre-trained scaler
    input_df[model_data["cols_to_scale"]] = model_data["scaler"].transform(
        input_df[model_data["cols_to_scale"]]
    )
    
    # Clean up temporary columns and unused features
    input_df = input_df.drop(cols_to_drop, axis=1)
    input_df = input_df.drop(['income', 'loan_amount'], axis=1)  # Remove original features
    
    # Ensure columns are in correct order for the model
    input_df = input_df[model.feature_names_in_]

    # # Make predictions
    # default_prob = round(model.predict_proba(input_df)[0][1], 2)  # Probability of default (class 1)
    # non_default_prob = 1 - default_prob  # Probability of non-default

    def calculate_credit_score(input_df, base_score=300, scale_length=600):
        x = np.dot(input_df.values, model.coef_.T) + model.intercept_
        default_probability = 1 / (1 + np.exp(-x))
        non_default_probability = 1 - default_probability

        credit_score = base_score + (non_default_probability.flatten() * scale_length)
        
        # Determine rating based on score ranges
        def get_rating(score):
            if credit_score < 500:
                return "Poor"
            elif 500 <= credit_score < 650:
                return "Average"
            elif 650 <= credit_score < 750:
                return "Good"
            elif 750 <= score <= 900:
                return "Excellent"
            else:
                return "Undefined"
                
        rating = get_rating(credit_score[0])
        return default_probability, credit_score, rating
    
    # Calculate final credit score and rating
    default_probability, credit_score, rating = calculate_credit_score(input_df)

    return round(default_probability.flatten()[0]*100, 2), int(credit_score), rating