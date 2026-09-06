import streamlit as st
import requests

st.title("Loan Risk Assessment")

loan_amnt = st.number_input("Loan Amount", min_value=0, value=15000)
term = st.selectbox("Term (months)", [36, 60])
int_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=12.5)
installment = st.number_input("Monthly Installment", min_value=0.0, value=500.0)
grade = st.selectbox("Credit Grade (1=A best, 7=G worst)", [1,2,3,4,5,6,7], index=1)
emp_length = st.slider("Employment Length (years)", 0, 10, 5)
annual_inc = st.number_input("Annual Income", min_value=0.0, value=60000.0)
dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, value=15.0)
open_acc = st.number_input("Open Credit Lines", min_value=0.0, value=10.0)
revol_bal = st.number_input("Revolving Balance", min_value=0, value=8000)
revol_util = st.number_input("Revolving Utilization (%)", min_value=0.0, value=40.0)
total_acc = st.number_input("Total Credit Lines", min_value=0.0, value=25.0)
home_ownership = st.selectbox("Home Ownership", ["MORTGAGE", "RENT", "OWN", "OTHER", "NONE"])
purpose = st.selectbox("Loan Purpose", ["debt_consolidation", "credit_card", "home_improvement",
    "major_purchase", "medical", "small_business", "vacation", "wedding", "moving",
    "house", "renewable_energy", "educational", "other"])

if st.button("Assess Risk"):
    payload = {
        "loan_amnt": loan_amnt, "term": term, "int_rate": int_rate, "installment": installment,
        "grade": grade, "emp_length": float(emp_length), "annual_inc": annual_inc, "dti": dti,
        "open_acc": open_acc, "revol_bal": revol_bal, "revol_util": revol_util, "total_acc": total_acc,
        "home_ownership_MORTGAGE": home_ownership == "MORTGAGE",
        "home_ownership_NONE": home_ownership == "NONE",
        "home_ownership_OTHER": home_ownership == "OTHER",
        "home_ownership_OWN": home_ownership == "OWN",
        "home_ownership_RENT": home_ownership == "RENT",
        "purpose_credit_card": purpose == "credit_card",
        "purpose_debt_consolidation": purpose == "debt_consolidation",
        "purpose_educational": purpose == "educational",
        "purpose_home_improvement": purpose == "home_improvement",
        "purpose_house": purpose == "house",
        "purpose_major_purchase": purpose == "major_purchase",
        "purpose_medical": purpose == "medical",
        "purpose_moving": purpose == "moving",
        "purpose_other": purpose == "other",
        "purpose_renewable_energy": purpose == "renewable_energy",
        "purpose_small_business": purpose == "small_business",
        "purpose_vacation": purpose == "vacation",
        "purpose_wedding": purpose == "wedding",
    }
    response = requests.post("https://credit-risk-api-piug.onrender.com/predict", json=payload)
    result = response.json()

    prob = result["default_probability"]
    risk = result["risk_category"]
    factors = result["top_factors"]

    st.metric("Default Probability", f"{prob*100:.1f}%")
    st.write("Risk Category:", risk)

    chart_data = {}
    for f in factors:
        chart_data[f["feature"]] = f["impact"]
    st.bar_chart(chart_data)
