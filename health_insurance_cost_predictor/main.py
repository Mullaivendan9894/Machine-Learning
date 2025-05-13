import streamlit as st
from prediction_helper import predict_premium, ohe_gender, ohe_region, ohe_marital_status, ohe_bmi_cat, ohe_smoking_status, ohe_emp_status


st.set_page_config(page_title="Insurance Cost Predictor", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: white;'>💼 Health Insurance Cost Predictor</h1>",
    unsafe_allow_html=True
)


# ---------------- PERSONAL DETAILS ----------------
with st.expander("👤 Personal Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Age", 18, 100)
    with col2:
        gender = st.selectbox("Gender", ohe_gender.categories_[0])
    with col3:
        region = st.selectbox("Region", ohe_region.categories_[0])

    col1, col2, col3 = st.columns(3)
    with col1:
        marital_status = st.selectbox("Marital Status", ohe_marital_status.categories_[0])
    with col2:
        number_of_dependants = st.slider("Number Of Dependants", min_value = 0, max_value = 10)
    with col3:
        employment_status = st.selectbox("Employment Status", ohe_emp_status.categories_[0])

    (col1,) = st.columns(1)
    with col1:
        income_lakhs = st.slider("Income in Lakhs", min_value = 0, max_value = 100)

# ---------------- HEALTH DETAILS ----------------
with st.expander("🏥 Health Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        bmi_category = st.selectbox("BMI Category", ohe_bmi_cat.categories_[0])
    with col2:
        smoking_status = st.selectbox("Smoking Status", ohe_smoking_status.categories_[0])
    with col3:
        genetical_risk = st.slider("Genetical Risk", min_value = 0, max_value = 5)

    col1, col2, col3 = st.columns(3)
    with col1:
        medical_history = st.selectbox("Medical History", ['Diabetes', 'High blood pressure', 'No Disease',
                                                           'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
                                                           'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                                                           'Diabetes & Heart disease'])
    with col2:
        insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])


# ---------------- PREDICT ----------------
st.markdown("---")
if st.button("🔍 Predict Premium"):
    user_input = {
        'age': age,
        'gender': gender,
        'region': region,
        'marital_status': marital_status,
        'number_of_dependants': number_of_dependants,
        'bmi_category': bmi_category,
        'smoking_status': smoking_status,
        'employment_status': employment_status,
        'income_level': 0,
        'income_lakhs': income_lakhs,
        'medical_history': medical_history,
        'insurance_plan': insurance_plan,
        'genetical_risk': genetical_risk
    }

    try:
        result = predict_premium(user_input)
        st.success(f"Predicted Insurance Premium: ₹{result:.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
