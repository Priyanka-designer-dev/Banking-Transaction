import streamlit as st
import pandas as pd
from db import get_connection
import os

st.set_page_config(page_title="Banking Transaction Analyzer", layout="wide")
st.title("🏦 Banking Transaction Analyzer")

conn = get_connection()

def load_data(query):
    return pd.read_sql(query, conn)

st.sidebar.header("Navigation")
view = st.sidebar.radio("Choose a view", ["Customers", "Accounts", "Transactions", "Summary"])

if view == "Customers":
    df = load_data("SELECT * FROM customers")
    st.subheader("👥 Customers")
    st.dataframe(df)

elif view == "Accounts":
    df = load_data("SELECT * FROM accounts")
    st.subheader("🏦 Accounts")
    st.dataframe(df)

elif view == "Transactions":
    df = load_data("SELECT * FROM transactions")
    st.subheader("💸 Transactions")
    st.dataframe(df)

elif view == "Summary":
    st.subheader("📊 Summary")
    total_customers = load_data("SELECT COUNT(*) FROM customers").iloc[0,0]
    total_accounts = load_data("SELECT COUNT(*) FROM accounts").iloc[0,0]
    total_transactions = load_data("SELECT COUNT(*) FROM transactions").iloc[0,0]
    total_balance = load_data("SELECT SUM(balance) FROM accounts").iloc[0,0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", total_customers)
    col2.metric("Total Accounts", total_accounts)
    col3.metric("Total Transactions", total_transactions)
    col4.metric("Total Balance", f"${total_balance:,.2f}")
