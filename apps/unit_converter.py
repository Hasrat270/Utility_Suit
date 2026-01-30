import streamlit as st


def run():
    st.header("📏 Smart Unit Converter")
    st.caption("Convert common units instantly")

    category = st.selectbox(
        "Choose Category",
        ["Length", "Weight", "Temperature"]
    )

    st.divider()

    # -----------------------------
    # Length Conversion
    # -----------------------------
    if category == "Length":
        col1, col2 = st.columns(2)

        with col1:
            km = st.number_input("Kilometers (km)", min_value=0.0, step=0.1)

        with col2:
            miles = km * 0.621371
            st.metric("Miles (mi)", f"{miles:.2f}")

    # -----------------------------
    # Weight Conversion
    # -----------------------------
    elif category == "Weight":
        col1, col2 = st.columns(2)

        with col1:
            kg = st.number_input("Kilograms (kg)", min_value=0.0, step=0.1)

        with col2:
            pounds = kg * 2.20462
            st.metric("Pounds (lb)", f"{pounds:.2f}")

    # -----------------------------
    # Temperature Conversion
    # -----------------------------
    elif category == "Temperature":
        col1, col2 = st.columns(2)

        with col1:
            celsius = st.number_input("Celsius (°C)", step=0.5)

        with col2:
            fahrenheit = (celsius * 9 / 5) + 32
            st.metric("Fahrenheit (°F)", f"{fahrenheit:.2f}")

    st.divider()
    st.caption("📌 Built as part of Mini App Hub")
