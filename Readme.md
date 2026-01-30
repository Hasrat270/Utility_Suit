# 🚀 Multi-Utility Suit

A modular Python web application built with **Streamlit** that brings together essential daily tools in one clean, dark-themed dashboard. This project is designed with a modular architecture, similar to **React's component-based structure**, making it highly scalable and easy to maintain.

## 🛠️ Features

- **🌤️ Real-Time Weather**: Fetches live weather data using the OpenWeatherMap API.
- **⚖️ BMI Calculator**: Calculate Body Mass Index with health category feedback.
- **🔑 Password Generator**: Generate secure, random passwords with customizable parameters.
- **💰 Expense Tracker**: Track daily spending with persistent session state management.
- **📏 Unit Converter**: Quickly convert between different measurements (Length, Weight, Temp).
- **🌑 Permanent Dark Mode**: Optimized for high-contrast viewing and eye comfort.

---

## 🏗️ Project Structure

The project follows a modular design pattern to separate logic from the main entry point:

```text
My_Hub/
├── main.py              # Application entry point & routing
├── apps/                # Components folder for mini-apps
│   ├── __init__.py      # Package initializer
│   ├── bmi.py
│   ├── weather.py
│   └── ...
├── .streamlit/
│   ├── config.toml      # Theme & UI configuration
│   └── secrets.toml     # API keys (local only)
├── requirements.txt     # Python dependencies
└── .gitignore           # Version control safety

```

🚀 Installation & Setup

1. Clone the repository
   Bash

git clone [https://github.com/your-username/multi-utility-suit.git](https://github.com/your-username/multi-utility-suit.git)
cd multi-utility-suit 2. Create and activate a virtual environment
Bash

# On Linux/macOS

python3 -m venv venv
source venv/bin/activate

# On Windows

python -m venv venv
.\venv\Scripts\activate 3. Install dependencies
Bash

pip install -r requirements.txt 4. Configure Secrets
Create a .streamlit/secrets.toml file and add your OpenWeatherMap API key:

Ini, TOML

OPENWEATHER_API_KEY = "your_api_key_here" 5. Run the app
Bash

streamlit run main.py
🌐 Deployment
This app is deployed on Streamlit Community Cloud. To protect sensitive data, API keys are managed through Streamlit's encrypted Secrets Management instead of being pushed to the public repository.

🗺️ Future Roadmap
As I progress in my Cybersecurity studies, I plan to add the following tools:

[ ] Hash Generator: Support for MD5, SHA-1, and SHA-256.

[ ] Password Strength Checker: Using entropy analysis.

[ ] Port Scanner: Simple network utility tool.

[ ] Subdomain Finder: Basic OSINT tool.

👨‍💻 Author
Hasrat

Education: BSSE Student (5th Semester Completed)

Experience: Software Engineering Intern at LA Consultancy

Tech Stack: MERN Stack, Python, Cybersecurity enthusiast
