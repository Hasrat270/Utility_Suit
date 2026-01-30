import streamlit as st
import random
import string

def run():
    st.header("🔑 Secure Password Generator")
    
    length = st.select_slider("Select Password Length", options=range(8, 33), value=12)
    
    use_digits = st.checkbox("Include Numbers", value=True)
    use_special = st.checkbox("Include Special Characters", value=True)
    
    if st.button("Generate Password", type="primary"):
        characters = string.ascii_letters
        if use_digits: characters += string.digits
        if use_special: characters += string.punctuation
        
        password = "".join(random.choice(characters) for _ in range(length))
        st.code(password, language="text")
        st.caption("Copy the password from the box above.")