import streamlit as st

# 1. Imports (Like importing components in React)
from apps import bmi, password_gen, unit_converter, weather, expense_tracker

st.set_page_config(page_title="Mini App Hub", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🚀 Navigation")
# List of apps for the selectbox
app_list = [
    "Dashboard", 
    "BMI Calculator", 
    "Password Generator", 
    "Unit Converter", 
    "Weather App", 
    "Expense Tracker"
]

choice = st.sidebar.selectbox("Choose an App", app_list)

# 3. Routing (Like React Router Switch)
if choice == "Dashboard":
    st.title("Welcome to My Hub")
    st.write("Select an app from the sidebar to start.")

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