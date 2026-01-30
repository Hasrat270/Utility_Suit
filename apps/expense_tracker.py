import streamlit as st

def run():
    st.header("💰 Smart Expense Tracker")
    st.write("Manage your daily spending and track your total budget.")

    # 1. Initialize State (Like 'const [expenses, setExpenses] = useState([])' in React)
    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    # 2. Input Form
    with st.form("expense_form", clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            item = st.text_input("What did you buy?")
        with col2:
            amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
        
        submitted = st.form_submit_button("Add to List", type="primary")
        
        if submitted and item:
            st.session_state.expenses.append({"item": item, "amount": amount})
            st.toast(f"Added {item}!") # Brief notification

    # 3. Data Processing (Derived State)
    total = sum(ex['amount'] for ex in st.session_state.expenses)

    # 4. Display UI
    if st.session_state.expenses:
        st.divider()
        
        # Summary Metric
        st.metric("Total Expenses", f"${total:.2f}")

        # Display History in a clean list
        st.write("### 📜 Transaction History")
        for i, ex in enumerate(reversed(st.session_state.expenses)):
            # We show newest first, like a real banking app
            st.write(f"**{ex['item']}** — `${ex['amount']:.2f}`")

        # 5. Reset Action
        st.write("---")
        if st.button("Clear All Data"):
            st.session_state.expenses = []
            st.rerun() # Forces a re-render to clear the screen
    else:
        st.info("No expenses recorded yet. Start by adding one above!")