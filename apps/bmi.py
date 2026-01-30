import streamlit as st
import plotly.graph_objects as go


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "🔵"
    elif bmi < 25:
        return "Normal Weight", "🟢"
    elif bmi < 30:
        return "Overweight", "🟠"
    else:
        return "Obese", "🔴"


def bmi_gauge(bmi):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=bmi,
            title={"text": "BMI Meter"},
            gauge={
                "axis": {"range": [0, 40]},
                "bar": {"thickness": 0.3},
                "steps": [
                    {"range": [0, 18.5], "color": "#87CEEB"},
                    {"range": [18.5, 25], "color": "#90EE90"},
                    {"range": [25, 30], "color": "#FFD580"},
                    {"range": [30, 40], "color": "#FF9999"},
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": bmi,
                },
            },
        )
    )
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig


def run():
    st.header("⚖️ Body Mass Index (BMI) Calculator")
    st.caption("Check your BMI and understand your health category")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input(
            "Weight (kg)", min_value=1.0, value=70.0, step=0.1
        )
    with col2:
        height = st.number_input(
            "Height (meters)", min_value=0.5, value=1.75, step=0.01
        )

    st.divider()

    if st.button("Calculate BMI", type="primary", use_container_width=True):
        bmi = weight / (height ** 2)
        category, emoji = bmi_category(bmi)

        st.subheader(f"Your BMI: **{bmi:.2f}**")
        st.write(f"### {emoji} Category: **{category}**")

        # Display Gauge Chart
        st.plotly_chart(bmi_gauge(bmi), use_container_width=True)

        # Health Tips
        if category == "Underweight":
            st.info("💡 Tip: Consider a nutrient-rich diet and consult a professional.")
        elif category == "Normal Weight":
            st.success("💡 Tip: Maintain your healthy lifestyle!")
        elif category == "Overweight":
            st.warning("💡 Tip: Regular exercise and balanced diet are recommended.")
        else:
            st.error("💡 Tip: Consult a healthcare provider for guidance.")

    st.divider()
    st.caption("📊 BMI is a general indicator and not a medical diagnosis.")
