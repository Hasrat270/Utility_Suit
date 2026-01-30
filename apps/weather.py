import streamlit as st
import requests

def run():
    st.header("🌤️ Live Weather App")
    city = st.text_input("Shehar ka naam likhein (e.g., Karachi, London):", "Karachi")
    import streamlit as st
import requests

def run():
    # Production mein ye line .streamlit/secrets.toml se key uthayegi
    API_KEY = st.secrets["OPENWEATHER_API_KEY"] 
    # ... baki code same rahega
    # OpenWeatherMap ki free API use kar sakte hain, abhi demo ke liye simple rakhte hain
    if st.button("Get Weather"):
        try:
            # Note: Real world mein aap yahan apni API Key dalenge
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=demo_key_ya_apki_key&units=metric"
            # Filhal logic:
            st.info(f"{city} ka weather check karne ke liye API key ki zaroorat hoti hai.")
            st.metric(label="Temperature", value="28 °C", delta="1.2 °C")
            st.write("Condition: Clear Sky")
        except:
            st.error("Shehar nahi mila!")