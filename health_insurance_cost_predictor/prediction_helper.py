import pandas as pd
import joblib
from joblib import load
import os
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
artifacts_path =  current_dir / "artifacts"


# Load all the models and encoders
model_rest = joblib.load(artifacts_path / "model_rest.joblib")
model_young = joblib.load(artifacts_path / "model_young.joblib")
scaler_rest = joblib.load(artifacts_path / "scaler_rest.joblib")
scaler_young = joblib.load(artifacts_path / "scaler_young.joblib")
ohe_gender = joblib.load(artifacts_path / "ohe_gender.joblib")
ohe_region = joblib.load(artifacts_path / "ohe_region.joblib")
ohe_marital_status = joblib.load(artifacts_path / "ohe_marital_status.joblib")
ohe_bmi_cat = joblib.load(artifacts_path / "ohe_bmi_cat.joblib")
ohe_smoking_status = joblib.load(artifacts_path / "ohe_smoking_status.joblib")
ohe_emp_status = joblib.load(artifacts_path / "ohe_emp_status.joblib")


risk_score = {
    "no disease": 0,
    "heart disease": 8,
    "diabetes": 6,
    'high blood pressure': 6,
    "thyroid": 5,
    "none":0
}

def predict_premium(user_input: dict):
     # Convert dict to DataFrame
    input_data_df = pd.DataFrame([user_input])
    

    # Medical history processing
    disease = input_data_df["medical_history"].str.lower().str.split("&")
    diseases = [i.strip() for item in disease for i in item]
    total_risk_score = sum(risk_score.get(dis,0) for dis in diseases)   

    min_score = 0
    max_score = 14
    normalized_risk_score = (total_risk_score - min_score ) / (max_score - min_score)
    input_data_df["normalized_risk_score"] = normalized_risk_score

    # Mapping ordinal features
    input_data_df["insurance_plan"] = input_data_df["insurance_plan"].map({"Bronze": 1, "Silver":2, "Gold": 3})

    # One-hot encoding
    gender_encoded_df = pd.DataFrame(ohe_gender.transform(input_data_df[["gender"]]), columns = ohe_gender.get_feature_names_out(["gender"]))
    region_encoded_df = pd.DataFrame(ohe_region.transform(input_data_df[["region"]]), columns = ohe_region.get_feature_names_out(["region"]))
    marital_encoded_df = pd.DataFrame(ohe_marital_status.transform(input_data_df[["marital_status"]]), columns = ohe_marital_status.get_feature_names_out(["marital_status"]))
    bmi_encoded_df = pd.DataFrame(ohe_bmi_cat.transform(input_data_df[["bmi_category"]]), columns = ohe_bmi_cat.get_feature_names_out(["bmi_category"]))
    smoking_encoded_df = pd.DataFrame(ohe_smoking_status.transform(input_data_df[["smoking_status"]]), columns = ohe_smoking_status.get_feature_names_out(["smoking_status"]))
    emp_encoded_df = pd.DataFrame(ohe_emp_status.transform(input_data_df[["employment_status"]]), columns = ohe_emp_status.get_feature_names_out(["employment_status"]))

    # Drop original categorical columns
    df_2_reset = input_data_df.drop(["gender", "region", "marital_status", "bmi_category", "smoking_status", "employment_status"], axis = 1).reset_index(drop = True)
    gender_encoded_df = gender_encoded_df.reset_index(drop=True)
    region_encoded_df = region_encoded_df.reset_index(drop=True)
    marital_encoded_df =marital_encoded_df.reset_index(drop=True)
    bmi_encoded_df = bmi_encoded_df.reset_index(drop=True)
    smoking_encoded_df = smoking_encoded_df.reset_index(drop=True)
    emp_encoded_df = emp_encoded_df.reset_index(drop = True)

    # Combine all features
    input_data_df = pd.concat([df_2_reset, gender_encoded_df, region_encoded_df, marital_encoded_df, bmi_encoded_df, smoking_encoded_df, emp_encoded_df], axis = 1)
    input_data_df = input_data_df.drop(["medical_history"], axis = 1)


    # Select model based on age
    if (input_data_df["age"] <= 25).any():
        feature_to_scale = scaler_young["features_to_scl"]
        input_data_df["income_level"] = 0
        input_data_df[feature_to_scale] = scaler_young["scaler"].transform(input_data_df[feature_to_scale])
        input_data_df.drop("income_level",  axis = 1, inplace = True)
        prediction = model_young.predict(input_data_df)
            
    else:
        feature_to_scale = scaler_rest["features_to_scl"]
        input_data_df["income_level"] = 0
        input_data_df[feature_to_scale] = scaler_rest["scaler"].transform(input_data_df[feature_to_scale])
        input_data_df.drop("income_level",  axis = 1, inplace = True)
        prediction = model_rest.predict(input_data_df)
    
    return prediction[0]

