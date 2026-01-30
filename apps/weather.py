import streamlit as st
import requests

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="Live Weather App", page_icon="🌤️", layout="centered")


def get_weather(city, api_key):
    """Fetch weather data from OpenWeather API"""
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url, timeout=10)
    return response


def run():
    st.header("🌤️ Live Weather App")
    st.caption("Real-time weather information using OpenWeather API")

    # -----------------------------
    # API Key (Secrets Management)
    # -----------------------------
    try:
        API_KEY = st.secrets["OPENWEATHER_API_KEY"]
    except KeyError:
        st.error("❌ API Key not found in secrets.toml!")
        st.stop()

    # -----------------------------
    # User Input
    # -----------------------------
    city = st.text_input("Enter city name:", "Karachi")

    # -----------------------------
    # Button Logic
    # -----------------------------
    if st.button("Get Weather", use_container_width=True):
        if not city.strip():
            st.warning("⚠️ Please enter a city name.")
            return

        try:
            response = get_weather(city, API_KEY)
            data = response.json()

            if response.status_code == 200:
                temp = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                desc = data["weather"][0]["description"].capitalize()
                icon = data["weather"][0]["icon"]

                st.success(f"Weather in {city.title()}")

                # Weather Icon
                icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
                st.image(icon_url, width=100)

                # Metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("🌡️ Temperature", f"{temp} °C")
                col2.metric("🤗 Feels Like", f"{feels_like} °C")
                col3.metric("💧 Humidity", f"{humidity}%")

                st.metric("💨 Wind Speed", f"{wind} m/s")
                st.write(f"**Condition:** {desc}")

            elif response.status_code == 404:
                st.error("❌ City not found. Please check the spelling.")

            else:
                st.error(f"⚠️ API Error: {data.get('message', 'Unknown error')}")

        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out. Please try again.")
        except requests.exceptions.ConnectionError:
            st.error("🌐 Network error. Check your internet connection.")
        except Exception as e:
            st.error(f"Unexpected Error: {e}")