import streamlit as st

def run():
    st.header("💰 Expense Tracker")
    
    # Initialize "State" if it doesn't exist
    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    with st.form("expense_form"):
        item = st.text_input("Item Name")
        amount = st.number_input("Amount", min_value=0)
        submitted = st.form_submit_button("Add Expense")
        
        if submitted:
            st.session_state.expenses.append({"item": item, "amount": amount})

    # Display List
    st.write("### History")
    for ex in st.session_state.expenses:
        st.write(f"- {ex['item']}: ${ex['amount']}")