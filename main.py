import streamlit as st

# --------------------------------------------------
# Page config MUST be the first Streamlit command
# --------------------------------------------------
st.set_page_config(
    page_title="Mini App Hub",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Imports (Like importing components in React)
# --------------------------------------------------
from apps import (
    bmi,
    password_gen,
    unit_converter,
    weather,
    expense_tracker
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("🚀 Navigation")

app_list = [
    "Dashboard",
    "BMI Calculator",
    "Password Generator",
    "Unit Converter",
    "Weather App",
    "Expense Tracker",
]

choice = st.sidebar.selectbox("Choose an App", app_list)

# --------------------------------------------------
# Routing (Like React Router Switch)
# --------------------------------------------------
if choice == "Dashboard":

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "https://avatars.githubusercontent.com/u/148011899?s=400&u=9ad699a123b8063215325fed9abf39c1f1a66667&v=4",
            width=160
        )

    with col2:
        st.title("Hasrat Afridi")
        st.markdown("### Software Engineering Student 🚀")
        st.markdown(
            "[🔗 Visit my GitHub Profile](https://github.com/Hasrat270)",
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("📌 Mini App Hub")
    st.write(
        "This hub contains multiple **utility applications** built using "
        "**Streamlit** with a **modular and scalable architecture**. "
        "Each app is designed as an independent module."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Total Apps", "5")
    col2.metric("🧩 Architecture", "Modular")
    col3.metric("🚀 Status", "Active")

    st.divider()

    st.subheader("🧠 Available Applications")
    st.markdown(
        """
        - ⚖️ **BMI Calculator** – Health indicator with visual meter  
        - 🔑 **Password Generator** – Secure password creation  
        - 📏 **Unit Converter** – Smart unit conversions  
        - 🌤️ **Weather App** – Live weather using OpenWeather API  
        - 💰 **Expense Tracker** – Track and manage daily expenses  
        """
    )

    st.divider()
    st.caption("Built by **Hasrat Afridi** • Powered by Streamlit 🚀")

# --------------------------------------------------
# Other Apps
# --------------------------------------------------
elif choice == "BMI Calculator":
    bmi.run()

elif choice == "Password Generator":
    password_gen.run()

elif choice == "Unit Converter":
    unit_converter.run()

elif choice == "Weather App":
    weather.run()

elif choice == "Expense Tracker":
    expense_tracker.run()
