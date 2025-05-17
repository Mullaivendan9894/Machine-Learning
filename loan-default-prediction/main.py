import streamlit as st
from prediction_helper import credit_risk_classification, ohe_loan_purpose, ohe_loan_type, ohe_resi_type

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Credit Risk Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
    .result-box { 
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .good-score { background-color: #4CAF50; color: white; }
    .average-score { background-color: #FFC107; color: black; }
    .poor-score { background-color: #F44336; color: white; }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown(
    "<h1 style='text-align: center; color: white;'>📊 Credit Risk Analyzer</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h6 style='text-align: center; color: gery;'>This tool helps financial institutions assess the creditworthiness of loan applicants.</h6>",
    unsafe_allow_html=True
)



# ========== INPUT FORM ==========
with st.expander("", expanded=True):
    st.subheader("🔍 Applicant Information")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", 18, 100, 30)
    with col2:
        income = st.number_input("Annual Income (₹)", min_value=1, value=50000, step=1000)
    with col3:
        loan_amount = st.number_input("Loan Amount (₹)", min_value=1, value=25000, step=1000)

    if income and income != 0:
        l_to_i = loan_amount / income
        st.metric("Loan to Income Ratio", f"{l_to_i:.2f}")

with st.expander("", expanded=True):
    st.subheader("📝 Loan Details")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_tenure_months = st.number_input("Loan Term (months)", 1, 120, 36)
    with col2:
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio", 0, 100, 30)
    with col3:
        number_of_open_accounts = st.number_input("Open Loan Accounts", min_value=0, value=2)

with st.expander("", expanded=True):
    st.subheader("⚠️ Risk Factors")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        delinquent_ratio = st.number_input("Delinquency Ratio", 0, 100, 5)
    with col2:
        avg_dpd_per_deliquency = st.number_input("Avg Days Past Due", min_value=0, value=0)
    with col3:
        residence_type = st.selectbox("Residence Type", ohe_resi_type.categories_[0])

    col1, col2 = st.columns(2)
    with col1:
        loan_purpose = st.selectbox("Loan Purpose", ohe_loan_purpose.categories_[0])
    with col2:
        loan_type = st.selectbox("Loan Type", ohe_loan_type.categories_[0])

# ========== CALCULATION ==========
if st.button("🔎 Assess Credit Risk", type="primary", use_container_width=True):
    input_data = {
        'age': age,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type,
        "loan_tenure_months": loan_tenure_months,
        "credit_utilization_ratio": credit_utilization_ratio,
        "loan_amount": loan_amount,
        "income": income,
        "number_of_open_accounts": number_of_open_accounts,
        "delinquent_ratio": delinquent_ratio,
        "avg_dpd_per_deliquency": avg_dpd_per_deliquency,
    }

    with st.spinner("Analyzing credit risk..."):
        try:
            default_prob, credit_score, rating = credit_risk_classification(input_data)
            default_prob = float(round(default_prob, 2))
            
            # ========== RESULTS DISPLAY ==========
            st.success("Analysis complete!")
            
            # Determine CSS class based on rating
            rating_class = {
                "Poor": "poor-score",
                "Average": "average-score",
                "Good": "good-score",
                "Excellent": "good-score"
            }.get(rating, "")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader("Default Probability", help="Lower is better")
                st.metric("", f"{default_prob}%")
            with col2:
                st.subheader("Credit Score", help="higher is better")
                delta_value = credit_score-600
                delta_str = f"{'+' if delta_value > 0 else ' '}{delta_value} from baseline"
                st.metric("", credit_score, 
                          delta=delta_str)
            with col3:
                st.markdown(f"""
                <div class="result-box {rating_class}">
                    <h3>Credit Rating</h3>
                    <h1>{rating}</h1>
                </div>
                """, unsafe_allow_html=True)
            
            
            # Add explanation
            with st.expander("ℹ️ What do these results mean?"):
                st.markdown("""
                - **Credit Score**: Ranges from 300-900 (higher is better)
                - **Default Probability**: Chance the applicant will default
                - **Rating**: Overall creditworthiness assessment
                """)
                
        except Exception as e:
            st.error(f"❌ Analysis failed: {str(e)}")
            st.exception(e)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("---")
    st.markdown("""
    ### About This Tool
    This application uses machine learning to predict:
    - Default probability
    - Credit score (300-900 scale)
    - Credit rating
    """)
    st.markdown("---")

