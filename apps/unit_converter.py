import streamlit as st

def run():
    st.header("📏 Smart Unit Converter")
    
    category = st.selectbox("Choose Category", ["Length", "Weight", "Temperature"])
    
    if category == "Length":
        val = st.number_input("Kilometers")
        st.write(f"Miles: {val * 0.621371:.2f}")
        
    elif category == "Weight":
        val = st.number_input("Kilograms")
        st.write(f"Pounds: {val * 2.20462:.2f}")
        
    elif category == "Temperature":
        val = st.number_input("Celsius")
        st.write(f"Fahrenheit: {(val * 9/5) + 32:.2f}")