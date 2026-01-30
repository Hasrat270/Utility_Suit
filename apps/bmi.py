import streamlit as st

def run():
    st.header("⚖️ Body Mass Index (BMI)")
    st.markdown("Enter your details below to calculate your BMI.")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0, step=0.1)
    with col2:
        height = st.number_input("Height (meters)", min_value=0.5, value=1.75, step=0.01)
    
    if st.button("Calculate BMI", type="primary"):
        bmi = weight / (height ** 2)
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Category: Normal Weight")
        elif 25 <= bmi < 30:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")