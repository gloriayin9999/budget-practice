import streamlit as st
from datetime import date

st.set_page_config(page_title="Teen Money", page_icon="💰", layout="wide")

# -----------------------------
# APP MEMORY
# -----------------------------
if "income" not in st.session_state:
    st.session_state.income = []

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "savings" not in st.session_state:
    st.session_state.savings = []


# -----------------------------
# TITLE
# -----------------------------
st.title("💰 Teen Money")
st.write("Track what you earn, spend, and save.")

st.subheader("September 2026")


# -----------------------------
# EARN + SPEND
# -----------------------------
earn_col, spend_col = st.columns(2)


# ===== EARN =====
with earn_col:

    st.header("💵 Earn")

    total_earned = sum(item["amount"] for item in st.session_state.income)

    st.metric("Total Earned", f"${total_earned:.2f}")

    job = st.text_input(
        "Job / Income Category",
        placeholder="Chick-fil-A, Lifeguard, Gift...",
        key="job"
    )

    income_amount = st.number_input(
        "Income Amount ($)",
        min_value=0.0,
        step=10.0,
        key="income_amount"
    )

    if st.button("➕ Add Income", use_container_width=True):

        if job and income_amount > 0:

            st.session_state.income.append(
                {
                    "date": str(date.today()),
                    "category": job,
                    "amount": income_amount
                }
            )

            st.success("Income added!")

    if st.session_state.income:

        st.write("### Income History")

        for item in st.session_state.income:
            st.write(
                item["date"],
                " | ",
                item["category"],
                " | $",
                item["amount"]
            )


# ===== SPEND =====
with spend_col:

    st.header("🛒 Spend")

    total_spent = sum(item["amount"] for item in st.session_state.expenses)

    st.metric("Total Spent", f"${total_spent:.2f}")

    spend_category = st.selectbox(
        "Spending Category",
        [
            "Food",
            "Gas",
            "Shopping",
            "Entertainment",
            "Other"
        ]
    )

    spend_amount = st.number_input(
        "Expense Amount ($)",
        min_value=0.0,
        step=5.0,
        key="spend_amount"
    )

    if st.button("➕ Add Expense", use_container_width=True):

        if spend_amount > 0:

            st.session_state.expenses.append(
                {
                    "date": str(date.today()),
                    "category": spend_category,
                    "amount": spend_amount
                }
            )

            st.success("Expense added!")

    if st.session_state.expenses:

        st.write("### Spending History")

        for item in st.session_state.expenses:
            st.write(
                item["date"],
                " | ",
                item["category"],
                " | $",
                item["amount"]
            )


# -----------------------------
# SAVING
# -----------------------------
st.divider()

st.header("🐷 Saving")

total_saved = sum(item["amount"] for item in st.session_state.savings)

st.metric("Total Saved", f"${total_saved:.2f}")

saving_col1, saving_col2 = st.columns(2)

with saving_col1:

    saving_category = st.text_input(
        "Saving Category",
        placeholder="College, Car, Emergency Fund..."
    )

with saving_col2:

    saving_amount = st.number_input(
        "Saving Amount ($)",
        min_value=0.0,
        step=10.0,
        key="saving_amount"
    )

if st.button("➕ Add Saving"):

    if saving_category and saving_amount > 0:

        st.session_state.savings.append(
            {
                "date": str(date.today()),
                "category": saving_category,
                "amount": saving_amount
            }
        )

        st.success("Saving added!")


if st.session_state.savings:

    st.write("### Saving History")

    for item in st.session_state.savings:
        st.write(
            item["date"],
            " | ",
            item["category"],
            " | $",
            item["amount"]
        )


# -----------------------------
# SUMMARY
# -----------------------------
st.divider()

st.header("📊 Monthly Summary")

col1, col2, col3, col4 = st.columns(4)

available_money = total_earned - total_spent - total_saved

col1.metric("Earned", f"${total_earned:.2f}")
col2.metric("Spent", f"${total_spent:.2f}")
col3.metric("Saved", f"${total_saved:.2f}")
col4.metric("Available", f"${available_money:.2f}")
