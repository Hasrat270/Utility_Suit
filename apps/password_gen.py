import streamlit as st
import random
import string


def generate_password(length, digits, special, exclude_ambiguous):
    chars = string.ascii_letters

    if digits:
        chars += string.digits

    if special:
        chars += string.punctuation

    if exclude_ambiguous:
        ambiguous = "lI1O0"
        chars = "".join(c for c in chars if c not in ambiguous)

    return "".join(random.choice(chars) for _ in range(length))


def password_strength(length, digits, special):
    score = length
    if digits:
        score += 5
    if special:
        score += 5

    if score < 15:
        return "Weak 🔴"
    elif score < 25:
        return "Medium 🟡"
    else:
        return "Strong 🟢"


def run():
    st.header("🔑 Secure Password Generator")
    st.caption("Generate strong and secure passwords instantly")

    col1, col2 = st.columns([2, 1])

    with col1:
        length = st.slider("Password Length", min_value=8, max_value=32, value=12)
        use_digits = st.checkbox("Include Numbers", value=True)
        use_special = st.checkbox("Include Special Characters", value=True)
        exclude_ambiguous = st.checkbox(
            "Exclude Ambiguous Characters (l, I, 1, O, 0)", value=True
        )

    with col2:
        strength = password_strength(length, use_digits, use_special)
        st.metric("Password Strength", strength)
        st.metric("Length", f"{length} characters")

    st.divider()

    if st.button("Generate Password", type="primary", use_container_width=True):
        password = generate_password(
            length, use_digits, use_special, exclude_ambiguous
        )

        st.success("Password Generated Successfully")
        st.code(password, language="text")
        st.caption("📋 Click to copy from the box above")

    st.divider()
    st.caption("🔐 Built with security best practices")


